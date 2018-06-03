from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^join$',views.join,name='join'),
	url(r'^login$',views.loginv,name='login'),
	url(r'^logout$',views.logoutv,name='logout'),
	url(r'^elist$',views.elist,name='elist'),
	url(r'^clist$',views.clist,name='clist'),
	url(r'^plist$',views.plist,name='plist'),

	url(r'^e1$',views.e1,name='e1'),	
	url(r'^e1/update$',views.e1update,name='e1update'),	
	url(r'^e1/delete/(\d+)/$',views.e1delete,name='e1delete'),	

	url(r'^ci$',views.ci,name='ci'),	
	url(r'^ci/update$',views.ci_update,name='ci_update'),	
	url(r'^ci/delete/(\d+)/$',views.ci_delete,name='ci_delete'),		

	url(r'^dc$',views.dc,name='dc'),	
	url(r'^dc/update$',views.dc_update,name='dc_update'),	
	url(r'^dc/delete/(\d+)/$',views.dc_delete,name='dc_delete'),		

	url(r'^da$',views.da,name='da'),	
	url(r'^da/update$',views.da_update,name='da_update'),	
	url(r'^da/delete/(\d+)/$',views.da_delete,name='da_delete'),		

	url(r'^gi$',views.gi,name='gi'),	
	url(r'^gi/update$',views.gi_update,name='gi_update'),	
	url(r'^gi/delete/(\d+)/$',views.gi_delete,name='gi_delete'),		

	url(r'^igi$',views.igi,name='igi'),	
	url(r'^igi/update$',views.igi_update,name='igi_update'),	
	url(r'^igi/delete/(\d+)/$',views.igi_delete,name='igi_delete'),		

	url(r'^si$',views.si,name='si'),	
	url(r'^si/update$',views.si_update,name='si_update'),	
	url(r'^si/delete/(\d+)/$',views.si_delete,name='si_delete'),		

	url(r'^wi$',views.wi,name='wi'),	
	url(r'^wi/update$',views.wi_update,name='wi_update'),	
	url(r'^wi/delete/(\d+)/$',views.wi_delete,name='wi_delete'),		

	url(r'^mi$',views.mi,name='mi'),	
	url(r'^mi/update$',views.mi_update,name='mi_update'),	
	url(r'^mi/delete/(\d+)/$',views.mi_delete,name='mi_delete'),		

	url(r'^hi$',views.hi,name='hi'),	
	url(r'^hi/update$',views.hi_update,name='hi_update'),	
	url(r'^hi/delete/(\d+)/$',views.hi_delete,name='hi_delete'),		

	url(r'^ahi$',views.ahi,name='ahi'),	
	url(r'^ahi/update$',views.ahi_update,name='ahi_update'),	
	url(r'^ahi/delete/(\d+)/$',views.ahi_delete,name='ahi_delete'),		

	url(r'^gsi$',views.gsi,name='gsi'),	
	url(r'^gsi/update$',views.gsi_update,name='gsi_update'),	
	url(r'^gsi/delete/(\d+)/$',views.gsi_delete,name='gsi_delete'),		
]

