from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse

def Beginning(request):
    return render(request,'Beginning.html')

def Corridor_I(request):
    return render(request,'Corridor_I.html')

def Corridor_II(request):
    return render(request,'Corridor_II.html')

def Toilet(request):
    return render(request,'Toilet.html')

def Department_office(request):
    return render(request,'Department_office.html')

def Five_A(request):
    return render(request,'5A.html')