from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model, authenticate, login
from django.views.decorators.http import require_POST
from .models import Profile, AuthenticationTable
from .forms import UserRegsiterForm
from uuid import uuid4
from django.conf import settings


def new_user_register(request, permission='admin'):
    if permission == 'admin' or request.user.is_authenticated:
        if (permission == 'voter' and request.user.is_manager) or (permission == 'manager' and request.user.is_staff) \
                or (permission == 'admin'):
            if request.method == 'POST':
                user_form = UserRegsiterForm(request.POST)
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
                form = UserRegsiterForm()
                return render(request, 'users/voter_register.html', {'form': form})
        else:
            return HttpResponse(status=405)


@require_POST
def user_auth(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return JsonResponse({'message': 'Missing parameters'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_key = AuthenticationTable(
            user=user,
            is_valid=True,
            key=uuid4().hex
        )
        auth_key.save()
        url = settings.BA
        return JsonResponse({'url': auth_key.key}, status=200)

    return JsonResponse({'message': 'Invalid username/password'}, status=401)


def move_auth_browser(request):
    key = request.GET['key']
    auth = get_object_or_404(AuthenticationTable, key=key)
    user = auth.user
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return HttpResponse(request, 'home_page.html', {})
