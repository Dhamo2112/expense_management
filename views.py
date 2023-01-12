from django.shortcuts import render
from django.http import HttpResponse
from EMapp.models import *


def home(request):
    obj = expense_management.objects.all()
    return render(request,"home.html",{"data":obj})