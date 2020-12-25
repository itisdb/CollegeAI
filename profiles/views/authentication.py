from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic.base import View

from profiles.models import Profile, User


class LoginView(View):

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                return render(request, 'pages/auth/login.html', {'error': 'Username/Password is incorrect.'})
            login(request, user)
            return redirect('profile:dashboard')
        return render(request, 'pages/auth/login.html', {'error': 'Username and Password is mandatory.'})

    def get(self, request):
        return render(request, 'pages/auth/login.html')


class RegisterView(View):

    def post(self, request):
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
        except (AttributeError, KeyError):
            return render(request, 'pages/auth/register.html', {'error': 'All fields are mandatory.'})
        user_obj = User.objects.create_user(username, email, password)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.save()
        Profile.objects.create(user=user_obj)
        user = authenticate(username=username, password=password)
        if not user:
            return render(request, 'pages/auth/login.html', {'error': 'Username/Password is incorrect.'})
        login(request, user)
        return redirect('profile:dashboard')

    def get(self, request):
        return render(request, 'pages/auth/register.html')
