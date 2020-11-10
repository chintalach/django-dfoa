from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import OwnerDetailsForms,TenantDetailsForms
from .models import owner_det,tenant_det

from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'ams/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'accounts/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'accounts/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def createownerdet(request):
    if request.method == 'GET':
        return render(request, 'ownerdetails/createownerdet.html', {'form':OwnerDetailsForms()})
    else:
        try:
            form = OwnerDetailsForms(request.POST)
            print(request.POST)
            newowner = form.save(commit=False)
            newowner.user = request.user
            newowner.save()
            return redirect('createownerdet')
        except ValueError:
            return render(request, 'ownerdetails/createownerdet.html', {'form':OwnerDetailsForms(), 'error':'Bad data passed in. Try again.'})


def createtenantdet(request):
    if request.method == 'GET':
        return render(request, 'tenantdetails/createtenantdet.html', {'form':TenantDetailsForms()})
    else:
        try:
            form = TenantDetailsForms(request.POST)
            print(request.POST)
            newowner = form.save(commit=False)
            newowner.user = request.user
            newowner.save()
            return redirect('createtenantdet')
        except ValueError:
            return render(request, 'tenantdetails/createtenantdet.html', {'form':TenantDetailsForms(), 'error':'Bad data passed in. Try again.'})

