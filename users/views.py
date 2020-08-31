from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from .models import Profile, AuthenticationTable
from .forms import UserRegisterForm, ProfileForm
from uuid import uuid4
from django.conf import settings


def new_user_register(request, permission='admin'):
    if permission == 'admin' or request.user.is_authenticated:
        if (permission == 'voter' and request.user.is_manager) or (permission == 'manager' and request.user.is_staff) \
                or (permission == 'admin'):
            if request.method == 'POST':
                user_form = UserRegisterForm(request.POST)
                if user_form.is_valid():
                    user_model = get_user_model()
                    user = user_model.objects.create_user(username=user_form.cleaned_data['username'],
                                                          email=user_form.cleaned_data['email'],
                                                          password=user_form.cleaned_data['password'])
                    user.first_name = user_form.cleaned_data['first_name']
                    user.last_name = user_form.cleaned_data['last_name']
                    if permission == 'voter':
                        user.is_voter = True
                    elif permission == 'manager':
                        user.is_manager = True
                    elif permission == 'admin':
                        user.is_staff = True

                    if permission == 'admin':
                        user.created_by = None
                    else:
                        user.created_by = request.user

                    user.save()
                    return render(request, 'users/register_successful.html', status=200)
                else:
                    return render(request, 'users/voter_register.html', {'form': user_form})
            elif request.method == 'GET':
                form = UserRegisterForm()
                return render(request, 'users/voter_register.html', {'form': form})
        else:
            return HttpResponse(status=405)


@require_POST
def user_auth(request):
    try:
        username = request.POST['username']
    except KeyError:
        return JsonResponse({'message': 'Missing required parameter username'}, status=400)

    user = get_object_or_404(get_user_model(), username=username)
    if user is not None:
        auth_key = AuthenticationTable(
            user=user,
            is_valid=True,
            key=uuid4().hex
        )
        auth_key.save()
        url = settings.BASE_URL + f'/users/validate/?key={auth_key.key}'
        return JsonResponse({'url': url}, status=200)

    return JsonResponse({'message': 'Invalid username/password'}, status=401)


@require_GET
def move_auth_browser(request):
    key = request.GET['key']
    auth = get_object_or_404(AuthenticationTable, key=key)
    auth.delete()
    user = auth.user
    login(request, user)
    # return HttpResponse(request, 'home_page.html', {})
    return HttpResponseRedirect('users/profile')


@login_required(login_url='users/login/')
@require_GET
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile_view.html', {'profile': profile})


@login_required(login_url='users/login/')
def profile_edit(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.admin_id = uuid4().hex
            profile.save()
            return render(request, 'managerVoteradd.html', {'form': ProfileForm(), 'message': 'Profile Updated Successfully'})
        else:
            return render(request, 'managerVoteradd.html', {'form': profile_form})
    else:
        form = ProfileForm()
        return render(request, 'managerVoteradd.html', {'form': form})
