from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib import messages
import bcrypt

def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already exists")
    return email

class UserManager(models.Manager):
    def register(self, **kwargs):
        error_list = []
        if not(kwargs['first_name'].isalpha() and kwargs['last_name'].isalpha()):
            error_list.append('Both name fields are required and can contain only letters.')
            messages.add_message(self.request, messages.INFO, 'Both name fields are required and can contain only letters.')
        if not validate_email(kwargs['email']):
            error_list.append('Invalid e-mail address entered. Please enter valid email address.')
            messages.add_message(self.request, messages.INFO, 'Invalid e-mail address entered. Please enter valid email address.')
        if len(kwargs['password']) < 8:
            error_list.append("Password must be at least eight characters in length")
            messages.add_message(self.request, messages.INFO, "Password must be at least eight characters in length")
        elif kwargs['password'] != kwargs['c_password']:
            error_list.append("Password and Password Confirmation do not match.")
            messages.add_message(self.request, messages.INFO, "Password and Password Confirmation do not match.")
        if len(error_list) is 0 :
            pw_hash = bcrypt.hashpw(kwargs['password'].encode, bcrypt.gensalt())
            user = self.create(first_name=kwargs['first_name'], last_name=kwargs['last_name'], email=kwargs['email'], password=pw_hash)
            return (True, user.id)
        else :
            print error_list
            return (False, error_list)

    # def login(self, **kwargs):



# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, validators=[validate_email,])
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Message(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    message_id = models.ForeignKey(Message)
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
