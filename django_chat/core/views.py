from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    context={}
    return render(request,'core/index.html',context)


def signup(request):
    # form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('index')
    else:
        form=SignupForm()

     
    return render(request,'core/signup.html',{"form":form})   


def login(request):
    return render(request,'core/login.html')
