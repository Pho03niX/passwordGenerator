from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html',{'password':'ajsdlkjasd'})


def eggs(request):
    return HttpResponse('<h1>eggsss</h1>')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html',{'password': thepassword})