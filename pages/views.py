from django.shortcuts import render
from .models import Login
from .forms import LoginForm

def index(request):
    x = {'name':'mohh', 'age':12345555645}
    return render(request, 'pages/index.html',x)

def login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        dataform = Login(username = username, password= password)
        dataform.save()     
   
    return render(request, 'pages/about.html',{'lf': LoginForm})