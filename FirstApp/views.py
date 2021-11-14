from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def munif(request):
    return render(request, 'munif.html',{'name':'Munif'})
def home(request):
    return render(request, 'home.html')
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    Result=val1+val2
    return render(request, 'result.html',{'result':Result,'number1':val1,'number2':val2})
def index(request):
    return render(request,'index.html')