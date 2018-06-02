from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^join$',views.join,name='join'),
	url(r'^login$',views.loginv,name='login'),
	url(r'^logout$',views.logoutv,name='logout'),
	url(r'^elist$',views.elist,name='elist'),

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
]

