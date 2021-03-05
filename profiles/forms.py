from django import forms 
from django.contrib.auth.models import User
from django.forms import ModelForm
from profiles.models import Profile 

class EditProfileForm(ModelForm):
         class Meta:
             model = User
             fields = (
                 'first_name',
                 'last_name',
                )

class ProfileForm(ModelForm): 
    class Meta: 
        model = Profile 
        fields = (
            'mobile_number',
        )


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length = 20,required=True)
    new_password = forms.CharField(max_length = 20,required=True)

class ResetPassword(forms.Form):
    new_password = forms.CharField(max_length = 20,required=True)
    confirm_password = forms.CharField(max_length = 20,required=True)

class EnterEmail(forms.Form):
    email = forms.EmailField(max_length = 30)