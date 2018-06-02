# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import e1model,com_infor,device_code,device_admin,gb_info,inner_gh_info,sensor_info
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


def ci_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		eid=int(request.POST['eid'])	
		if eid!=0:
			getd=com_infor.objects.get(id=eid)
			getd.CI_CODE=a
			getd.CI_NAME=b
			getd.CI_ADDR=c
			getd.CI_PHONE=d
			getd.save()
		else:
			data=com_infor(CI_CODE=a,CI_NAME=b,CI_ADDR=c,CI_PHONE=d)
			data.save()
		return redirect('ci')
	if 'id' in request.GET:
		data=get_object_or_404(com_infor,id=request.GET['id'])
		return render(request,"farm/ci_update.html",{'d':data})
	return render(request,"farm/ci_update.html",{})

def ci(request):
	ds=com_infor.objects.all()
	return render(request,"farm/ci.html",{"ds":ds})

def ci_delete(request,eid):
	getd=com_infor.objects.get(id=eid)
	getd.delete()
	return redirect('ci')


def dc_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		eid=int(request.POST['eid'])	
		if eid!=0:
			getd=device_code.objects.get(id=eid)
			getd.DC_CODE=a
			getd.DC_KIND=b
			getd.save()
		else:
			data=device_code(DC_CODE=a,DC_KIND=b)
			data.save()
		return redirect('dc')
	if 'id' in request.GET:
		data=get_object_or_404(device_code,id=request.GET['id'])
		return render(request,"farm/dc_update.html",{'d':data})
	return render(request,"farm/dc_update.html",{})


def dc(request):
	ds=device_code.objects.all()
	return render(request,"farm/dc.html",{"ds":ds})

def dc_delete(request,eid):
	getd=device_code.objects.get(id=eid)
	getd.delete()
	return redirect('dc')

def da(request):
	ds=device_admin.objects.all()
	return render(request,"farm/da.html",{"ds":ds})

def da_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=int(request.POST['e'])
		e=com_infor.objects.get(id=e)
		eid=int(request.POST['eid'])
		if eid!=0:
			getd=device_admin.objects.get(id=eid)
			getd.DA_ID=a
			getd.DA_NAME=b
			getd.DA_PHONE=c
			getd.DA_ROLE=d
			getd.CI_ID=e
			getd.save()
		else:
			data=device_admin(DA_ID=a,DA_NAME=b,DA_PHONE=c,DA_ROLE=d,CI_ID=e)
			data.save()
		return redirect('da')
	if 'id' in request.GET:
		data=get_object_or_404(device_admin,id=request.GET['id'])
		ds=com_infor.objects.all()
		return render(request,"farm/da_update.html",{'d':data,'ds':ds})

	ds=com_infor.objects.all()
	return render(request,"farm/da_update.html",{'ds':ds})


def da_delete(request,eid):
	getd=device_admin.objects.get(id=eid)
	getd.delete()
	return redirect('da')



def gi(request):
	ds=gb_info.objects.all()
	return render(request,"farm/gi.html",{"ds":ds})



def gi_update(request):
	if request.method=="POST":
		a=int(request.POST['a'])
		a=e1model.objects.get(id=a)
		
		b=request.POST['b']
		c=request.POST['c']
		d=float(request.POST['d'])
		e=float(request.POST['e'])
		f=float(request.POST['f'])
		g=request.POST['g']
		h=request.POST['h']
		i=request.POST['i']
		j=request.POST['j']
		k=request.POST['k']
		l=request.POST['l']
		m=request.POST['m']
		n=request.POST['n']
		o=request.POST['o']
		
		p=int(request.POST['p'])
		p=device_admin.objects.get(id=p)

		eid=int(request.POST['eid'])

		if eid!=0:
			getd=gb_info.objects.get(id=eid)
			getd.FI_ID=a
			getd.GB_NUMBER=b
			getd.GB_KIND_CODE=c
			getd.GB_FA_LATITUDE=d
			getd.GB_FA_LONGITUDE=e
			getd.GB_SIZE=f
			getd.GB_ARCHITECTURE=g
			getd.GB_CONT_KIND=h
			getd.GB_INSTALL_DIAGRM=i
			getd.GB_DIGITAL_MANUAL=j
			getd.GB_FA_LAND_CATER=k
			getd.GB_CENTER_DIRECT=l
			getd.GB_INSTAL=m
			getd.GB_MANUFA=n
			getd.GB_MAINTE_COMP=o
			getd.DA_ID=p
			getd.save()
		else:
			data=gb_info(FI_ID=a,GB_NUMBER=b,GB_KIND_CODE=c,GB_FA_LATITUDE=d,GB_FA_LONGITUDE=e,GB_SIZE=f,GB_ARCHITECTURE=g,GB_CONT_KIND=h,GB_INSTALL_DIAGRM=i,GB_DIGITAL_MANUAL=j,GB_FA_LAND_CATER=k,GB_CENTER_DIRECT=l,GB_INSTAL=m,GB_MANUFA=n,GB_MAINTE_COMP=o,DA_ID=p)
			data.save()

		return redirect('gi')
	if 'id' in request.GET:
		data=get_object_or_404(gb_info,id=request.GET['id'])
		ds1=e1model.objects.all()
		ds2=device_admin.objects.all()
		return render(request,"farm/gi_update.html",{'d':data,'ds1':ds1,'ds2':ds2})

	ds1=e1model.objects.all()
	ds2=device_admin.objects.all()
	return render(request,"farm/gi_update.html",{'ds1':ds1,'ds2':ds2})


def gi_delete(request,eid):
	getd=gb_info.objects.get(id=eid)
	getd.delete()
	return redirect('gi')


