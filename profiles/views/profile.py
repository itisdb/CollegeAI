from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

from college.models import CollegeBookmark
from profiles.models import OTPVerification, Profile
from profiles.forms import ProfileForm,EditProfileForm,ResetPassword,EnterEmailForm
from profiles.forms import ChangePasswordForm

from base.generic_mailer import generic_mailer

import random

from tracker.log_to_tracker import log_to_tracker


class ForgotPassword(View):

    def get(self, request, username, otp):
        return render(request, 'v2/pages/protected/reset_password.html')

    def post(self, request, username, otp):
        user = User.objects.get(username=username)
        form = ResetPassword(request.POST)
        profile = Profile.objects.get(user = user)
        otp_object = OTPVerification.objects.get(
                profile=profile,
                otp=otp,
                verifier_tag=OTPVerification.VerifierTag.PASSWORD_RESET.value,
                is_verified=False
            )
        otp_object.is_verified = True
        otp_object.save()
        if form.is_valid():
            user.set_password(form.data.get('new_password'))
            user.save()
            return HttpResponseRedirect('/profile/dashboard')
        else:
            messages.info(request, 'Confirm password and new password not matching!!')
        return render(request, 'v2/pages/protected/reset_password.html')


class EnterEmail(View):

    def get(self, request):
        return render(request, 'v2/pages/protected/enter-email.html',{}) 

    def post(self, request):
        form = EnterEmailForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            user = User.objects.filter(email=email).first()
            if user:
                username = user.username
                profile = Profile.objects.get(user = user)
                otp_object, _ = OTPVerification.objects.get_or_create(
                profile=profile,
                otp=str(random.randint(100000, 999999)),
                verifier_tag=OTPVerification.VerifierTag.PASSWORD_RESET.value,
                is_verified=False
                )
                link = '/reset-password/{}/{}'.format(
                username,
                otp_object.otp
                ),
                print(link)
                context = {
                'template_name' : 'forgot-password-mail.html',
                'recipients' : email,
                'username':username,
                'link':link,
                'full_name':user.first_name,
                }
                try:
                    generic_mailer(context)
                except:
                    pass
                messages.info(request, 'Mail has been sent to you succesfully!!')
            else:
                messages.info(request, 'No profile exists with such email!!')
        else:
            print('No')
        return render(request, 'v2/pages/protected/enter-email.html', {})


class Dashboard(View):

    def get(self, request, *args, **kwargs):
        log_to_tracker(request, 'dashboard')
        bookmarks = CollegeBookmark.objects.all()
        return render(request, 'v2/raw/dashboard.html', {'bookmarks': bookmarks})


class EditUserProfileView(View):

    def get(self, request, format=None):
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        context = {
            'form':form,
            'profile_form': profile_form,
        }
        return render(request, 'v2/pages/protected/edit-profile.html', context) 


    def post(self, request, format=None):
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile) 
       
        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            messages.success(request, 'Changed Successfully!!')
        context = {
            'form':form,
            'profile_form': profile_form,
        }

        return render(request, 'v2/pages/protected/edit-profile.html', context) 


class UpdatePassword(View):

    def get(self, request,  format=None):
        return render(request, 'v2/pages/protected/update-password.html', {}) 

    def post(self, request, format=None):
        user = request.user
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            old_password = form.data.get('old_password')
            if not user.check_password(old_password):
               messages.success(request, 'Wrong Password!!')
            else:
                user.set_password(form.data.get('new_password'))
                user.save()
                messages.success(request, 'Changed Successfully!!')
        context = {
            'form':form,
        }
        return render(request, 'v2/pages/protected/update-password.html', context)
