# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import e1model
# Create your views here.

def index(request):
	return render(request,"farm/index.html",{'user':request.user})


def join(request):
	if request.method=="POST":
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		u=User.objects.create_user(username=username,password=password,email=email)
		login(request,u)
		return render(request,"farm/complete.html",{'msg':'회원가입이 완료되었습니다.'})
	return render(request,"farm/join.html",{})

def loginv(request):
	if request.method == "POST" :
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('index')
		else:
			return render(request,"farm/complete.html",{'msg':'로그인에 실패했습니다.'})
	else:
		return render(request,"farm/login.html",{})

def logoutv(request):
	if request.user.is_authenticated:
		logout(request)
	return redirect('index')

def elist(request):
	return render(request,"farm/elist.html",{})

def e1(request):
	ds=e1model.objects.all()
	return render(request,"farm/e1.html",{"ds":ds})

def e1update(request):
	
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']
		f=request.POST['f']
		g=request.POST['g']
		h=int(request.POST['h'])
		i=int(request.POST['i'])
		j=request.POST['j']
		eid=int(request.POST['eid'])	
		if eid != 0:
			getd=e1model.objects.get(id=eid)
			getd.GB_FA_ID=a
			getd.GB_FA_PW=b
			getd.CTVT_FCLTY_ID=c
			getd.GB_FA_PHONE=d
			getd.GB_FA_EMAIL=e
			getd.GB_FA_ADDR=f
			getd.GB_FA_NAME=g
			getd.GB_FA_SIZE=h
			getd.GB_FAM_NUM=i
			getd.GB_COOPER_UNIT=j
			getd.save()
		else:
			data=e1model(GB_FA_ID=a,GB_FA_PW=b,CTVT_FCLTY_ID=c,GB_FA_PHONE=d,GB_FA_EMAIL=e,GB_FA_ADDR=f,GB_FA_NAME=g,GB_FA_SIZE=h,GB_FAM_NUM=i,GB_COOPER_UNIT=j)
			data.save()
		return redirect('e1')
	if 'id' in request.GET:
		data=get_object_or_404(e1model,id=request.GET['id'])
		return render(request,"farm/e1update.html",{'d':data})
	return render(request,"farm/e1update.html",{})

def e1delete(request,eid):
	getd=e1model.objects.get(id=eid)
	getd.delete()
	return redirect('e1')