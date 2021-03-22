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

    def clean(self):
        cleaned_data = super(ResetPassword, self).clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError(
                "new_password and confirm_password does not match"
            )

class EnterEmailForm(forms.Form):
    email = forms.EmailField(max_length = 30)