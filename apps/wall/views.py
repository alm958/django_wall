from django.shortcuts import render, redirect
from .models import User, Message, Comment
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def index(request):
    UForm = UserForm(request.POST or None)
    context = {
        'UserForm': UForm
    }
    return render(request, 'wall/index.html', context )

def login(request):
    if request.method == 'POST':
        User.objects.login(request.POST)

def register(request):
    if request.method == 'POST':
        User.objects.register(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'],c_password=request.POST['c_password'])
