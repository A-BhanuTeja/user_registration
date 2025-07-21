from django import forms

from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']




'''
While we are sending Parent Tables FOrm Object and
Child Tables FOrm Object into same HTML page 
then we should not represent Parent Tables column in 
Input Elements
'''