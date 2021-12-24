from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Client
from .forms import ClientForm
from custom import rand


def index(request):
    return render(request, 'plep_app/index.html')

def start(request):
    return render(request, 'plep_app/start.html')

def register(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        uid = rand.uniqid(10)
        form.uid = uid
        if form.is_valid():
            form.save()
            return redirect('register')
  
    context = {'form':form}
    return render(request, 'plep_app/register.html', context)

def uid(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        if uid is not None:
            return redirect('dashboard', pk=uid)

    return render(request, 'plep_app/uid.html')

def dashboard(request, pk):
    client = Client.objects.get(uid=pk)
    context = {'client':client}
    return render(request, 'plep_app/dashboard.html', context)