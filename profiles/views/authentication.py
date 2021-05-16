from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic.base import View
from profiles.models import Profile, User
from base.generic_mailer import generic_mailer


class LoginView(View):

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                return render(request, 'v2/pages/public/home.html', {'error': 'Username/Password is incorrect.'})
            login(request, user)
            return redirect('profile:dashboard')
        return render(request, 'v2/pages/public/home.html', {'error': 'Username and Password is mandatory.'})

    def get(self, request):
        return render(request, 'v2/pages/public/home.html')


class RegisterView(View):

    def post(self, request):
        try:
            name = request.POST['name']
            name = name.split(" ", 1)
            first_name = name[0]
            last_name = name[-1]
            username = request.POST['username']
            password = request.POST['password']
        except (AttributeError, KeyError):
            return render(request, 'v2/pages/public/home.html', {'error': 'All fields are mandatory.'})
        try:
            user_obj = User.objects.create_user(username, username, password)
        except BaseException:
            return render(request, 'v2/pages/public/home.html', {'error': 'Username already exists.'})
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.save()
        user = authenticate(username=username, password=password)
        if not user:
            return render(request, 'v2/pages/public/home.html', {'error': 'Username/Password is incorrect.'})
        login(request, user)
        context = {
            'template_name': 'welcome_mail.html',
            'recipients': username,
            'username': username,
            'first_name': first_name,
        }
        try:
            generic_mailer(**context)
        except:
            pass
        return redirect('profile:dashboard')

    def get(self, request):
        return render(request, 'v2/pages/public/home.html')


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'v2/pages/public/home.html', {'message': 'You have been logged out !'})


class ResetPasswordView(View):
    pass


