from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from .models import Profile, AuthenticationTable, CustomUser
from .forms import UserRegisterForm, ProfileForm
from uuid import uuid4
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess


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
                    if request.user.is_authenticated:
                        if request.user.is_manager == True:
                            user.is_voter = True
                            user.created_by = request.user
                        elif request.user.is_admin == True:
                            user.is_manager = True
                            user.created_by = request.user
                    else:
                        user.is_staff = True
                        user.created_by = None
                    user.save()
                    #Call fingerprint enroller
                    # program = 'C:/Users/Bosipo/Documents/digivot-finger/digivot-finger/Fingerprint Authentication/bin/Release/Fingerprint Authentication.exe'
                    # subprocess.call([program,'functionToExecute','enroll','userID',str(user.id)])
                    return render(request, 'users/register_successful.html')
                else:
                    return render(request, 'users/voter_register.html', {'form': user_form})
            elif request.method == 'GET':
                form = UserRegisterForm()
                return render(request, 'users/voter_register.html', {'form': form})
        else:
            return HttpResponse(status=405)


# @require_GET
# def login_to_browser(request, key):
#     auth = get_object_or_404(AuthenticationTable, key=key)
#     if auth.is_valid:
#         user = auth.user
#         auth.delete()
#         login(request, user)
#         if user.is_voter:
#             return HttpResponseRedirect('/application/votersLanding/')
#         elif user.is_manager:
#             return HttpResponseRedirect('/application/managerDash/')
#         elif user.is_staff:
#             return HttpResponseRedirect('/application/adminDash/')
#         else:
#             return HttpResponse(status=403)
#     else:
#         return HttpResponse(status=403)
def login_user(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'index.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            #Call fingerprint enroller
            # program = 'C:/Users/Bosipo/Documents/digivot-finger/digivot-finger/Fingerprint Authentication/bin/Release/Fingerprint Authentication.exe'
            # subprocess.call([program,'functionToExecute','verify','userID',str(user.id)])
            login(request, user)
            if user.is_voter:
                return HttpResponseRedirect('/application/votersLanding/')
            elif user.is_manager:
                return HttpResponseRedirect('/application/manager/dashboard/')
            elif user.is_staff:
                return HttpResponseRedirect('/application/admin/dashboard/')
            else:
                return HttpResponse(status=403)
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'index.html', {'context': context})


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
            return render(request,
                          'managerVoteradd.html',
                          {'form': ProfileForm(), 'message': 'Profile Updated Successfully'})
        else:
            return render(request, 'managerVoteradd.html', {'form': profile_form})
    else:
        form = ProfileForm()
        return render(request, 'managerVoteradd.html', {'form': form})



@require_POST
def account_logout(request):
    logout(request)
    return render(request, 'index.html', {})


def account_login(request):
    return render(request, 'index.html', {})
