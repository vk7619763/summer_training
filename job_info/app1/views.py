# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1 import forms

def studentview(request):
    form=forms.studentform()
    return render(request,"app1/studentform.html",{'form':form})


# Create your views here.
