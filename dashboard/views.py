# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import e1model,com_infor,device_code,device_admin,gb_info,inner_gh_info,sensor_info,work_info,mainte_info,harves_info,after_harves_info,sale_info,plan_stages,seedling_plan,storage,germination,grafting,crop_info,image_info,dip_info,nursery_info,seedling_date
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

def clist(request):
	return render(request,"farm/clist.html",{})

def plist(request):
	return render(request,"farm/plist.html",{})

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



def igi(request):
	ds=inner_gh_info.objects.all()
	return render(request,"farm/igi.html",{"ds":ds})


def igi_update(request):
	if request.method=="POST":
		a=request.POST['a']
		c=int(request.POST['c'])
		c=gb_info.objects.get(id=c)
		d=request.POST['d']
		e=request.POST['e']
		f=request.POST['f']
		g=request.POST['g']

		eid=int(request.POST['eid'])

		if eid!=0:
			getd=inner_gh_info.objects.get(id=eid)
			getd.GB_DONG_NUMBER=a
			getd.GB_INFO_ID=c
			getd.GB_KIND_CROP=d
			getd.GB_INNER_SIZE=e
			getd.GB_INNER_KIND=f
			getd.GB_INNER_DEVI_LOC=g
			getd.save()
		else:
			data=inner_gh_info(GB_DONG_NUMBER=a,GB_INFO_ID=c,GB_KIND_CROP=d,GB_INNER_SIZE=e,GB_INNER_KIND=f,GB_INNER_DEVI_LOC=g)
			data.save()

		return redirect('igi')
	if 'id' in request.GET:
		data=get_object_or_404(inner_gh_info,id=request.GET['id'])
		ds=gb_info.objects.all()
		return render(request,"farm/igi_update.html",{'d':data,'ds':ds})

	ds=gb_info.objects.all()
	return render(request,"farm/igi_update.html",{'ds':ds})


def igi_delete(request,eid):
	getd=inner_gh_info.objects.get(id=eid)
	getd.delete()
	return redirect('igi')


def si(request):
	ds=sensor_info.objects.all()
	return render(request,"farm/si.html",{"ds":ds})


def si_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		
		d=int(request.POST['d'])
		d=device_code.objects.get(id=d)

		e=int(request.POST['e'])
		e=com_infor.objects.get(id=e)

		f=int(request.POST['f'])
		f=inner_gh_info.objects.get(id=f)		
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=sensor_info.objects.get(id=eid)
			getd.SI_ID=a
			getd.SI_KIND=b
			getd.SI_ACTU_CODE=c
			getd.DC_ID=d
			getd.CI_ID=e
			getd.IGI_ID=f
			getd.save()
		else:
			data=sensor_info(SI_ID=a,SI_KIND=b,SI_ACTU_CODE=c,DC_ID=d,CI_ID=e,IGI_ID=f)
			data.save()

		return redirect('si')
	if 'id' in request.GET:
		data=get_object_or_404(sensor_info,id=request.GET['id'])
		ds1=device_code.objects.all()
		ds2=com_infor.objects.all()
		ds3=inner_gh_info.objects.all()
		return render(request,"farm/si_update.html",{'d':data,'ds1':ds1,'ds2':ds2,'ds3':ds3})

	ds1=device_code.objects.all()
	ds2=com_infor.objects.all()
	ds3=inner_gh_info.objects.all()
	return render(request,"farm/si_update.html",{'ds1':ds1,'ds2':ds2,'ds3':ds3})


def si_delete(request,eid):
	getd=sensor_info.objects.get(id=eid)
	getd.delete()
	return redirect('si')


def wi(request):
	ds=work_info.objects.all()
	return render(request,"farm/wi.html",{"ds":ds})


def wi_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']
		f=request.POST['f']
		g=request.POST['g']
		h=request.POST['h']
		
		i=int(request.POST['i'])
		i=e1model.objects.get(id=i)

		j=int(request.POST['j'])
		j=gb_info.objects.get(id=j)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=work_info.objects.get(id=eid)
			getd.GM_WORK_ID=a
			getd.GM_WORK_DATE=b
			getd.GM_WORK_LINE_NUM=c
			getd.GM_LABOR_TIME=d
			getd.GM_WORK_INFO=e
			getd.GM_AGRI_MTRI_IN_WORK=f
			getd.GM_WORK_CODE=g
			getd.GM_WORK_OP=h
			getd.FI_ID=i
			getd.CI_ID=j
			getd.save()
		else:
			data=work_info(GM_WORK_ID=a,GM_WORK_DATE=b,GM_WORK_LINE_NUM=c,GM_LABOR_TIME=d,GM_WORK_INFO=e,GM_AGRI_MTRI_IN_WORK=f,GM_WORK_CODE=g,GM_WORK_OP=h,FI_ID=i,CI_ID=j)
			data.save()

		return redirect('wi')
	if 'id' in request.GET:
		data=get_object_or_404(work_info,id=request.GET['id'])
		ds1=e1model.objects.all()
		ds2=gb_info.objects.all()
		return render(request,"farm/wi_update.html",{'d':data,'ds1':ds1,'ds2':ds2})

	ds1=e1model.objects.all()
	ds2=gb_info.objects.all()
	return render(request,"farm/wi_update.html",{'ds1':ds1,'ds2':ds2})

def wi_delete(request,eid):
	getd=work_info.objects.get(id=eid)
	getd.delete()
	return redirect('wi')


def mi(request):
	ds=mainte_info.objects.all()
	return render(request,"farm/mi.html",{"ds":ds})


def mi_update(request):
	if request.method=="POST":
		a=int(request.POST['a'])
		a=work_info.objects.get(id=a)

		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=mainte_info.objects.get(id=eid)
			getd.WI_ID=a
			getd.GM_MAINTE_WORKE_DATE=b
			getd.GM_FACITY_NAME=c
			getd.GM_MAINTE_INFO=d
			getd.GM_REPAIR_COST=e
			getd.save()
		else:
			data=mainte_info(WI_ID=a,GM_MAINTE_WORKE_DATE=b,GM_FACITY_NAME=c,GM_MAINTE_INFO=d,GM_REPAIR_COST=e)
			data.save()

		return redirect('mi')
	if 'id' in request.GET:
		data=get_object_or_404(mainte_info,id=request.GET['id'])
		ds1=work_info.objects.all()
		return render(request,"farm/mi_update.html",{'d':data,'ds1':ds1})

	ds1=work_info.objects.all()
	return render(request,"farm/mi_update.html",{'ds1':ds1})

def mi_delete(request,eid):
	getd=mainte_info.objects.get(id=eid)
	getd.delete()
	return redirect('mi')

def hi(request):
	ds=harves_info.objects.all()
	return render(request,"farm/hi.html",{"ds":ds})


def hi_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']

		f=int(request.POST['f'])
		f=work_info.objects.get(id=f)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=harves_info.objects.get(id=eid)
			getd.GM_HARVES_ID=a
			getd.GM_DATE_HARVES=b
			getd.GM_HARVES_YIELD=c
			getd.GM_WEIGHT=d
			getd.GM_QUALIT_GRAD=e
			getd.WI_ID=f
			getd.save()
		else:
			data=harves_info(GM_HARVES_ID=a,GM_DATE_HARVES=b,GM_HARVES_YIELD=c,GM_WEIGHT=d,GM_QUALIT_GRAD=e,WI_ID=f)
			data.save()

		return redirect('hi')
	if 'id' in request.GET:
		data=get_object_or_404(harves_info,id=request.GET['id'])
		ds1=work_info.objects.all()
		return render(request,"farm/hi_update.html",{'d':data,'ds1':ds1})

	ds1=work_info.objects.all()
	return render(request,"farm/hi_update.html",{'ds1':ds1})

def hi_delete(request,eid):
	getd=harves_info.objects.get(id=eid)
	getd.delete()
	return redirect('hi')

def ahi(request):
	ds=after_harves_info.objects.all()
	return render(request,"farm/ahi.html",{"ds":ds})


def ahi_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']

		c=int(request.POST['c'])
		c=harves_info.objects.get(id=c)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=after_harves_info.objects.get(id=eid)
			getd.GM_LOT_NUM=a
			getd.GM_INFO_PROCESS=b
			getd.HI_ID=c
			getd.save()
		else:
			data=after_harves_info(GM_LOT_NUM=a,GM_INFO_PROCESS=b,HI_ID=c)
			data.save()

		return redirect('ahi')
	if 'id' in request.GET:
		data=get_object_or_404(after_harves_info,id=request.GET['id'])
		ds1=harves_info.objects.all()
		return render(request,"farm/ahi_update.html",{'d':data,'ds1':ds1})

	ds1=harves_info.objects.all()
	return render(request,"farm/ahi_update.html",{'ds1':ds1})

def ahi_delete(request,eid):
	getd=after_harves_info.objects.get(id=eid)
	getd.delete()
	return redirect('ahi')


def gsi(request):
	ds=sale_info.objects.all()
	return render(request,"farm/gsi.html",{"ds":ds})


def gsi_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']
		f=request.POST['f']
		g=request.POST['g']
		h=int(request.POST['h'])
		h=harves_info.objects.get(id=h)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=sale_info.objects.get(id=eid)
			getd.GM_SALE_ID=a
			getd.GM_SALE_DATE=b
			getd.GM_METHODS_SALE=c
			getd.GM_PACK_UNIT=d
			getd.GM_GALSE=e
			getd.GM_PRICE_BOX=f
			getd.GM_TOTAL_INCOME=g
			getd.HI_ID=h
			getd.save()
		else:
			data=sale_info(GM_SALE_ID=a,GM_SALE_DATE=b,GM_METHODS_SALE=c,GM_PACK_UNIT=d,GM_GALSE=e,GM_PRICE_BOX=f,GM_TOTAL_INCOME=g,HI_ID=h)
			data.save()

		return redirect('gsi')
	if 'id' in request.GET:
		data=get_object_or_404(sale_info,id=request.GET['id'])
		ds1=harves_info.objects.all()
		return render(request,"farm/gsi_update.html",{'d':data,'ds1':ds1})

	ds1=harves_info.objects.all()
	return render(request,"farm/gsi_update.html",{'ds1':ds1})

def gsi_delete(request,eid):
	getd=sale_info.objects.get(id=eid)
	getd.delete()
	return redirect('gsi')