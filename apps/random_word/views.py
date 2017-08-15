# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    try:
        request.session['count'] += 1
    except Exception as e:
        request.session['count'] = 0
    aString = get_random_string(length=14)
    context = { "rndWord" : aString  }
    return render(request, "random_word/index.html", context)

def reset(request):
    request.session['count'] = 0
    return redirect('/')
