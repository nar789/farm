# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import *

# Create your views here.

def index(request):
	return render(request,"farm/index3.html",{'user':request.user})


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

def glist(request):
	return render(request,"farm/glist.html",{})

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

def ps(request):
	ds=plan_stages.objects.all()
	return render(request,"farm/ps.html",{"ds":ds})


def ps_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=int(request.POST['b'])
		b=e1model.objects.get(id=b)
		c=int(request.POST['c'])
		c=gb_info.objects.get(id=c)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=plan_stages.objects.get(id=eid)
			getd.PS_PLAN_CODE=a
			getd.FI_ID=b
			getd.GI_ID=c
			getd.save()
		else:
			data=plan_stages(PS_PLAN_CODE=a,FI_ID=b,GI_ID=c)
			data.save()

		return redirect('ps')
	if 'id' in request.GET:
		data=get_object_or_404(plan_stages,id=request.GET['id'])
		ds1=e1model.objects.all()
		ds2=gb_info.objects.all()
		return render(request,"farm/ps_update.html",{'d':data,'ds1':ds1,'ds2':ds2})

	ds1=e1model.objects.all()
	ds2=gb_info.objects.all()
	return render(request,"farm/ps_update.html",{'ds1':ds1,'ds2':ds2})

def ps_delete(request,eid):
	getd=plan_stages.objects.get(id=eid)
	getd.delete()
	return redirect('ps')


def sp(request):
	ds=seedling_plan.objects.all()
	return render(request,"farm/sp.html",{"ds":ds})


def sp_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']
		f=request.POST['f']
		g=request.POST['g']
		h=request.POST['h']
		i=request.POST['i']
		j=request.POST['j']
		k=request.POST['k']

		l=int(request.POST['l'])
		l=plan_stages.objects.get(id=l)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=seedling_plan.objects.get(id=eid)
			getd.SP_ID=a
			getd.SP_DATE=b
			getd.SP_TRAY=c
			getd.SP_GROW_MEDIA=d
			getd.SP_PRODUCTION=e
			getd.SP_SEEDING_DATE=f
			getd.SP_GRAFTING_DATE=g
			getd.SP_SCION_GRAFT=h
			getd.SP_ROOT_GRAFT=i
			getd.SP_GRAFT_TAKE=j
			getd.SP_SHIPPING_DATE=k
			getd.PS_ID=l
			getd.save()
		else:
			data=seedling_plan(SP_ID=a,SP_DATE=b,SP_TRAY=c,SP_GROW_MEDIA=d,SP_PRODUCTION=e,SP_SEEDING_DATE=f,SP_GRAFTING_DATE=g,SP_SCION_GRAFT=h,SP_ROOT_GRAFT=i,SP_GRAFT_TAKE=j,SP_SHIPPING_DATE=k,PS_ID=l)
			data.save()

		return redirect('sp')
	if 'id' in request.GET:
		data=get_object_or_404(seedling_plan,id=request.GET['id'])
		ds1=plan_stages.objects.all()
		return render(request,"farm/sp_update.html",{'d':data,'ds1':ds1})

	ds1=plan_stages.objects.all()
	return render(request,"farm/sp_update.html",{'ds1':ds1})

def sp_delete(request,eid):
	getd=seedling_plan.objects.get(id=eid)
	getd.delete()
	return redirect('sp')


def st(request):
	ds=storage.objects.all()
	return render(request,"farm/st.html",{"ds":ds})


def st_update(request):
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
		i=plan_stages.objects.get(id=i)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=storage.objects.get(id=eid)
			getd.ST_STORAGE_ID=a
			getd.ST_TEMP=b
			getd.ST_PERIOD=c
			getd.ST_QUALITY=d
			getd.ST_RESP_COEF=e
			getd.ST_RESP_RATE=f
			getd.ST_RESP_LOSS=g
			getd.ST_SURV_RATE=h
			getd.PS_ID=i
			getd.save()
		else:
			data=storage(ST_STORAGE_ID=a,ST_TEMP=b,ST_PERIOD=c,ST_QUALITY=d,ST_RESP_COEF=e,ST_RESP_RATE=f,ST_RESP_LOSS=g,ST_SURV_RATE=h,PS_ID=i)
			data.save()

		return redirect('st')
	if 'id' in request.GET:
		data=get_object_or_404(storage,id=request.GET['id'])
		ds1=plan_stages.objects.all()
		return render(request,"farm/st_update.html",{'d':data,'ds1':ds1})

	ds1=plan_stages.objects.all()
	return render(request,"farm/st_update.html",{'ds1':ds1})

def st_delete(request,eid):
	getd=storage.objects.get(id=eid)
	getd.delete()
	return redirect('st')


def ge(request):
	ds=germination.objects.all()
	return render(request,"farm/ge.html",{"ds":ds})


def ge_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']

		f=int(request.POST['f'])
		f=plan_stages.objects.get(id=f)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=germination.objects.get(id=eid)
			getd.GE_ID=a
			getd.GE_RATE=b
			getd.GE_ENERGY=c
			getd.GE_DAYS=d
			getd.GE_UNIFORMITY=e
			getd.PS_ID=f
			getd.save()
		else:
			data=germination(GE_ID=a,GE_RATE=b,GE_ENERGY=c,GE_DAYS=d,GE_UNIFORMITY=e,PS_ID=f)
			data.save()

		return redirect('ge')
	if 'id' in request.GET:
		data=get_object_or_404(germination,id=request.GET['id'])
		ds1=plan_stages.objects.all()
		return render(request,"farm/ge_update.html",{'d':data,'ds1':ds1})

	ds1=plan_stages.objects.all()
	return render(request,"farm/ge_update.html",{'ds1':ds1})

def ge_delete(request,eid):
	getd=germination.objects.get(id=eid)
	getd.delete()
	return redirect('ge')


def gr(request):
	ds=grafting.objects.all()
	return render(request,"farm/gr.html",{"ds":ds})


def gr_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=int(request.POST['c'])
		c=plan_stages.objects.get(id=c)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=grafting.objects.get(id=eid)
			getd.GR_ID=a
			getd.GR_TAKE_RATE=b
			getd.PS_ID=c
			getd.save()
		else:
			data=grafting(GR_ID=a,GR_TAKE_RATE=b,PS_ID=c)
			data.save()

		return redirect('gr')
	if 'id' in request.GET:
		data=get_object_or_404(grafting,id=request.GET['id'])
		ds1=plan_stages.objects.all()
		return render(request,"farm/gr_update.html",{'d':data,'ds1':ds1})

	ds1=plan_stages.objects.all()
	return render(request,"farm/gr_update.html",{'ds1':ds1})

def gr_delete(request,eid):
	getd=grafting.objects.get(id=eid)
	getd.delete()
	return redirect('gr')


def cr(request):
	ds=crop_info.objects.all()
	return render(request,"farm/cr.html",{"ds":ds})


def cr_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']
		f=request.POST['f']
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=crop_info.objects.get(id=eid)
			getd.CI_INFO_ID=a
			getd.CI_VEGETABLES=b
			getd.CI_NG_SEEDING_VAR=c
			getd.CI_SCION_VAR=d
			getd.CI_INFO_GATHER=e
			getd.CI_GATHER_CODE=f
			getd.save()
		else:
			data=crop_info(CI_INFO_ID=a,CI_VEGETABLES=b,CI_NG_SEEDING_VAR=c,CI_SCION_VAR=d,CI_INFO_GATHER=e,CI_GATHER_CODE=f)
			data.save()

		return redirect('cr')
	if 'id' in request.GET:
		data=get_object_or_404(crop_info,id=request.GET['id'])
		return render(request,"farm/cr_update.html",{'d':data})

	return render(request,"farm/cr_update.html",{})

def cr_delete(request,eid):
	getd=crop_info.objects.get(id=eid)
	getd.delete()
	return redirect('cr')

def ii(request):
	ds=image_info.objects.all()
	return render(request,"farm/ii.html",{"ds":ds})


def ii_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=request.POST['e']
		f=request.POST['f']
		g=int(request.POST['g'])
		g=crop_info.objects.get(id=g)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=image_info.objects.get(id=eid)
			getd.IMI_ID=a
			getd.IMI_DEVICE_CODE=b
			getd.IMI_SNAP_DATE=c
			getd.IMI_RESOLUTION=d
			getd.IMI_IPIAI=e
			getd.IMI_RAW_DATA=f
			getd.CI_ID=g
			getd.save()
		else:
			data=image_info(IMI_ID=a,IMI_DEVICE_CODE=b,IMI_SNAP_DATE=c,IMI_RESOLUTION=d,IMI_IPIAI=e,IMI_RAW_DATA=f,CI_ID=g)
			data.save()

		return redirect('ii')
	if 'id' in request.GET:
		data=get_object_or_404(image_info,id=request.GET['id'])
		ds1=crop_info.objects.all()
		return render(request,"farm/ii_update.html",{'d':data,'ds1':ds1})

	ds1=crop_info.objects.all()
	return render(request,"farm/ii_update.html",{'ds1':ds1})

def ii_delete(request,eid):
	getd=image_info.objects.get(id=eid)
	getd.delete()
	return redirect('ii')


def dip(request):
	ds=dip_info.objects.all()
	return render(request,"farm/dip.html",{"ds":ds})


def dip_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']
		e=int(request.POST['e'])
		e=crop_info.objects.get(id=e)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=dip_info.objects.get(id=eid)
			getd.DIP_ID=a
			getd.D_ID=b
			getd.I_ID=c
			getd.P_ID=d
			getd.CI_ID=e
			getd.save()
		else:
			data=dip_info(DIP_ID=a,D_ID=b,I_ID=c,P_ID=d,CI_ID=e)
			data.save()

		return redirect('dip')
	if 'id' in request.GET:
		data=get_object_or_404(dip_info,id=request.GET['id'])
		ds1=crop_info.objects.all()
		return render(request,"farm/dip_update.html",{'d':data,'ds1':ds1})

	ds1=crop_info.objects.all()
	return render(request,"farm/dip_update.html",{'ds1':ds1})

def dip_delete(request,eid):
	getd=dip_info.objects.get(id=eid)
	getd.delete()
	return redirect('dip')


def sd(request):
	ds=seedling_date.objects.all()
	return render(request,"farm/sd.html",{"ds":ds})


def sd_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		
		d=int(request.POST['d'])
		d=plan_stages.objects.get(id=d)

		e=int(request.POST['e'])
		e=crop_info.objects.get(id=e)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=seedling_date.objects.get(id=eid)
			getd.SD_PROCESS_ID=a
			getd.SD_START_DATE=b
			getd.SD_END_DATE=c
			getd.PS_ID=d
			getd.CI_ID=e
			getd.save()
		else:
			data=seedling_date(SD_PROCESS_ID=a,SD_START_DATE=b,SD_END_DATE=c,PS_ID=d,CI_ID=e)
			data.save()

		return redirect('sd')
	if 'id' in request.GET:
		data=get_object_or_404(seedling_date,id=request.GET['id'])
		ds1=plan_stages.objects.all()
		ds2=crop_info.objects.all()
		return render(request,"farm/sd_update.html",{'d':data,'ds1':ds1,'ds2':ds2})

	ds1=plan_stages.objects.all()
	ds2=crop_info.objects.all()
	return render(request,"farm/sd_update.html",{'ds1':ds1,'ds2':ds2})

def sd_delete(request,eid):
	getd=seedling_date.objects.get(id=eid)
	getd.delete()
	return redirect('sd')



def ni(request):
	ds=nursery_info.objects.all()
	return render(request,"farm/ni.html",{"ds":ds})


def ni_update(request):
	if request.method=="POST":
		a=request.POST['a']
		b=request.POST['b']
		c=request.POST['c']
		d=request.POST['d']

		e=int(request.POST['e'])
		e=crop_info.objects.get(id=e)
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=nursery_info.objects.get(id=eid)
			getd.NI_SEDDING_ID=a
			getd.NI_PH=b
			getd.NI_LN=c
			getd.NI_LL=d
			getd.CI_ID=e
			getd.save()
		else:
			data=nursery_info(NI_SEDDING_ID=a,NI_PH=b,NI_LN=c,NI_LL=d,CI_ID=e)
			data.save()

		return redirect('ni')
	if 'id' in request.GET:
		data=get_object_or_404(nursery_info,id=request.GET['id'])
		ds1=crop_info.objects.all()
		return render(request,"farm/ni_update.html",{'d':data,'ds1':ds1})

	ds1=crop_info.objects.all()
	return render(request,"farm/ni_update.html",{'ds1':ds1})

def ni_delete(request,eid):
	getd=nursery_info.objects.get(id=eid)
	getd.delete()
	return redirect('ni')



def g1(request):
	ds=nutrient_state.objects.all()
	return render(request,"farm/g1.html",{"ds":ds})


def g1_update(request):
	if request.method=="POST":
		a=int(request.POST['a'])
		a=gb_info.objects.get(id=a)
		b=request.POST['b']
		c=request.POST['c']
		d=float(request.POST['d'])
		e=float(request.POST['e'])
		f=float(request.POST['f'])
		g=float(request.POST['g'])
		h=float(request.POST['h'])
		i=float(request.POST['i'])
		j=float(request.POST['j'])
		k=float(request.POST['k'])
		
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=nutrient_state.objects.get(id=eid)
			getd.GB_INNER_FA_ID=a
			getd.GE_SUPPLY_START_TIME=b
			getd.GE_SUPPLY_END_TIME=c
			getd.GE_WATER_OUT=d
			getd.GE_SUPPLY_EC=e
			getd.GE_SUPPLY_PH=f
			getd.GE_SPLY_CONST_CONCEN=g
			getd.GE_FLOW_OUT=h
			getd.GE_DRAIN_EC=i
			getd.GE_DRAIN_PH=j
			getd.GE_DRAIN_CONST_CONCEN=k
			getd.save()
		else:
			data=nutrient_state(GB_INNER_FA_ID=a,GE_SUPPLY_START_TIME=b,GE_SUPPLY_END_TIME=c,GE_WATER_OUT=d,GE_SUPPLY_EC=e,
				GE_SUPPLY_PH=f,GE_SPLY_CONST_CONCEN=g,GE_FLOW_OUT=h,GE_DRAIN_EC=i,GE_DRAIN_PH=j,GE_DRAIN_CONST_CONCEN=k)
			data.save()

		return redirect('g1')
	if 'id' in request.GET:
		data=get_object_or_404(nutrient_state,id=request.GET['id'])
		ds1=gb_info.objects.all()
		return render(request,"farm/g1_update.html",{'d':data,'ds1':ds1})

	ds1=gb_info.objects.all()
	return render(request,"farm/g1_update.html",{'ds1':ds1})

def g1_delete(request,eid):
	getd=nutrient_state.objects.get(id=eid)
	getd.delete()
	return redirect('g1')

def g2(request):
	ds=onoff_act.objects.all()
	return render(request,"farm/g2.html",{"ds":ds})


def g2_update(request):
	if request.method=="POST":
		a=int(request.POST['a'])
		a=gb_info.objects.get(id=a)
		b=request.POST['b']
		c=bool(int(request.POST['c']))
		d=bool(int(request.POST['d']))
		e=bool(int(request.POST['e']))
		f=bool(int(request.POST['f']))
		g=bool(int(request.POST['g']))
		h=bool(int(request.POST['h']))
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=onoff_act.objects.get(id=eid)
			getd.GB_INNER_FA_ID=a
			getd.GB_EVENT_TIME=b
			getd.GE_FAN=c
			getd.GE_SUPPORT_LIGHT=d
			getd.GE_HEAT=e
			getd.GE_IRRIGA=f
			getd.GE_CO2_GE=g
			getd.GE_FOG=h
			getd.save()
		else:
			data=onoff_act(GB_INNER_FA_ID=a,GB_EVENT_TIME=b,GE_FAN=c,GE_SUPPORT_LIGHT=d,GE_HEAT=e,
				GE_IRRIGA=f,GE_CO2_GE=g,GE_FOG=h)
			data.save()

		return redirect('g2')
	if 'id' in request.GET:
		data=get_object_or_404(onoff_act,id=request.GET['id'])
		ds1=gb_info.objects.all()
		return render(request,"farm/g2_update.html",{'d':data,'ds1':ds1})

	ds1=gb_info.objects.all()
	return render(request,"farm/g2_update.html",{'ds1':ds1})

def g2_delete(request,eid):
	getd=onoff_act.objects.get(id=eid)
	getd.delete()
	return redirect('g2')

def g3(request):
	ds=actuator.objects.all()
	return render(request,"farm/g3.html",{"ds":ds})


def g3_update(request):
	if request.method=="POST":
		a=int(request.POST['a'])
		a=gb_info.objects.get(id=a)
		b=request.POST['b']
		c=bool(int(request.POST['c']))
		d=bool(int(request.POST['d']))
		e=bool(int(request.POST['e']))
		f=bool(int(request.POST['f']))
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=actuator.objects.get(id=eid)
			getd.GB_INNER_FA_ID=a
			getd.GE_ACTION_TIME=b
			getd.GE_TOP_VENT=c
			getd.GE_SIDE_VENT=d
			getd.GE_HORIZN_CURTAN=e
			getd.GE_VERTICAL_CURTAN=f
			getd.save()
		else:
			data=actuator(GB_INNER_FA_ID=a,GE_ACTION_TIME=b,GE_TOP_VENT=c,GE_SIDE_VENT=d,GE_HORIZN_CURTAN=e,
				GE_VERTICAL_CURTAN=f)
			data.save()

		return redirect('g3')
	if 'id' in request.GET:
		data=get_object_or_404(actuator,id=request.GET['id'])
		ds1=gb_info.objects.all()
		return render(request,"farm/g3_update.html",{'d':data,'ds1':ds1})

	ds1=gb_info.objects.all()
	return render(request,"farm/g3_update.html",{'ds1':ds1})

def g3_delete(request,eid):
	getd=actuator.objects.get(id=eid)
	getd.delete()
	return redirect('g3')

def g4(request):
	ds=env_root.objects.all()
	return render(request,"farm/g4.html",{"ds":ds})


def g4_update(request):
	if request.method=="POST":
		a=int(request.POST['a'])
		a=gb_info.objects.get(id=a)
		b=request.POST['b']
		c=float(request.POST['c'])
		d=float(request.POST['d'])
		e=float(request.POST['e'])
		f=float(request.POST['f'])
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=env_root.objects.get(id=eid)
			getd.GB_INNER_FA_ID=a
			getd.GE_ROOT_TIME=b
			getd.GE_GROUND_TEMP=c
			getd.GE_GROUND_HUMI=d
			getd.GE_EC=e
			getd.GE_PH=f
			getd.save()
		else:
			data=env_root(GB_INNER_FA_ID=a,GE_ROOT_TIME=b,GE_GROUND_TEMP=c,GE_GROUND_HUMI=d,GE_EC=e,
				GE_PH=f)
			data.save()

		return redirect('g4')
	if 'id' in request.GET:
		data=get_object_or_404(env_root,id=request.GET['id'])
		ds1=gb_info.objects.all()
		return render(request,"farm/g4_update.html",{'d':data,'ds1':ds1})

	ds1=gb_info.objects.all()
	return render(request,"farm/g4_update.html",{'ds1':ds1})

def g4_delete(request,eid):
	getd=env_root.objects.get(id=eid)
	getd.delete()
	return redirect('g4')

def g5(request):
	ds=env_outer.objects.all()
	return render(request,"farm/g5.html",{"ds":ds})


def g5_update(request):
	if request.method=="POST":
		a=int(request.POST['a'])
		a=gb_info.objects.get(id=a)
		b=request.POST['b']
		c=float(request.POST['c'])
		d=float(request.POST['d'])
		e=float(request.POST['e'])
		f=float(request.POST['f'])
		g=float(request.POST['g'])
		h=float(request.POST['h'])
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=env_outer.objects.get(id=eid)
			getd.GB_INNER_FA_ID=a
			getd.GB_OUT_TIME=b
			getd.GE_OUT_TEMP=c
			getd.GE_OUT_HUMI=d
			getd.GE_OUT_WIND_DIRECT=e
			getd.GE_OUT_WIND_SPD=f
			getd.GE_SOLAR_RADI=g
			getd.GE_RAINF=h
			getd.save()
		else:
			data=env_outer(GB_INNER_FA_ID=a,GB_OUT_TIME=b,GE_OUT_TEMP=c,GE_OUT_HUMI=d,GE_OUT_WIND_DIRECT=e,
				GE_OUT_WIND_SPD=f,GE_SOLAR_RADI=g,GE_RAINF=h)
			data.save()

		return redirect('g5')
	if 'id' in request.GET:
		data=get_object_or_404(env_outer,id=request.GET['id'])
		ds1=gb_info.objects.all()
		return render(request,"farm/g5_update.html",{'d':data,'ds1':ds1})

	ds1=gb_info.objects.all()
	return render(request,"farm/g5_update.html",{'ds1':ds1})

def g5_delete(request,eid):
	getd=env_outer.objects.get(id=eid)
	getd.delete()
	return redirect('g5')

def g6(request):
	ds=env_inner.objects.all()
	return render(request,"farm/g6.html",{"ds":ds})


def g6_update(request):
	if request.method=="POST":
		a=int(request.POST['a'])
		a=gb_info.objects.get(id=a)
		b=request.POST['b']
		c=float(request.POST['c'])
		d=float(request.POST['d'])
		e=float(request.POST['e'])
		f=float(request.POST['f'])
		g=float(request.POST['g'])
		
		eid=int(request.POST['eid'])

		if eid!=0:
			getd=env_inner.objects.get(id=eid)
			getd.GB_INNER_FA_ID=a
			getd.GE_IN_TIME=b
			getd.GE_IN_TEMP=c
			getd.GE_IN_HUMI=d
			getd.GE_IN_CO2=e
			getd.GE_IN_SOLAR_RADI=f
			getd.GE_IN_WIND_SPD=g
			getd.save()
		else:
			data=env_inner(GB_INNER_FA_ID=a,GE_IN_TIME=b,GE_IN_TEMP=c,GE_IN_HUMI=d,GE_IN_CO2=e,
				GE_IN_SOLAR_RADI=f,GE_IN_WIND_SPD=g)
			data.save()

		return redirect('g6')
	if 'id' in request.GET:
		data=get_object_or_404(env_inner,id=request.GET['id'])
		ds1=gb_info.objects.all()
		return render(request,"farm/g6_update.html",{'d':data,'ds1':ds1})

	ds1=gb_info.objects.all()
	return render(request,"farm/g6_update.html",{'ds1':ds1})

def g6_delete(request,eid):
	getd=env_inner.objects.get(id=eid)
	getd.delete()
	return redirect('g6')