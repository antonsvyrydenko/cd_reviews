# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("index")
    return render(request, 'main/home.html')

def info(request):
    #return HttpResponse("index")
    return render(request, 'main/about.html', {'values':['this blog is about cd and artists reviews','be fair, love your cat and listen to music']})

def latest(request):
	return render(request, 'news/posts.html')
