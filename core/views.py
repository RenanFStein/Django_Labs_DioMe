from email import message
import imp
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as django_login

def login(request):
    return render (request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            message.error(request, 'Usuario/Senha inválidos. Por favor tente novamente')
    return redirect('login')
