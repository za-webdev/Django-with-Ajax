# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.core import serializers
from models import Post

def index(request):

	return render (request,'ajax_posts/index.html')

def create(request):
	Post.objects.create(
	content=request.POST['content'])
	posts=Post.objects.all().order_by('-created_at')

	return render (request,'ajax_posts/display.html',{'posts':posts})
