from django import forms
from .models import User, Message, Comment

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
