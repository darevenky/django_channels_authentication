from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.forms import *
# Create your views here.

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'app/home.html',d)
    return render(request,'app/home.html')


def registration(request):
    ufo=UserForm()
    d={'ufo':ufo}

    if request.method=='POST':
        UFO=UserForm(request.POST)

        if UFO.is_valid():
            USUO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            USUO.set_password(password)
            USUO.save()

            return HttpResponse('registration is succefull')
        else:
            return HttpResponse('not valid data')
    return render(request,'app/registration.html',d)



def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('data not valid')
    return render(request,'app/user_login.html')



@login_required
def index(request):
    return render(request, "app/index.html")

@login_required
def room(request, room_name):
    return render(request, "app/room.html", {"room_name": room_name})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
