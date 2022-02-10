from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from app.models import Profile

from authentication.app.models import Profile
from app.models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).first():
            messages.success(request,'username already exists')
            return redirect('/register')

        if User.objects.filter(email =email).first():
            messages.success(request, 'Email already exists')
            return redirect('/register')

        user_obj = User.objects.create(username = username, email = email)
        user_obj.set_password(password)

        profile_obj = Profile.objects.create(user = user)
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')

def token_send(request):
    return render(request, 'token_send.html')