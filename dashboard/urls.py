from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^join$',views.e1update,name='join'),
	url(r'^login$',views.loginv,name='login'),
	url(r'^logout$',views.logoutv,name='logout'),
	url(r'^elist$',views.elist,name='elist'),
	url(r'^clist$',views.clist,name='clist'),
	url(r'^plist$',views.plist,name='plist'),
	url(r'^glist$',views.glist,name='glist'),

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

	url(r'^ps$',views.ps,name='ps'),	
	url(r'^ps/update$',views.ps_update,name='ps_update'),	
	url(r'^ps/delete/(\d+)/$',views.ps_delete,name='ps_delete'),		

	url(r'^sp$',views.sp,name='sp'),	
	url(r'^sp/update$',views.sp_update,name='sp_update'),	
	url(r'^sp/delete/(\d+)/$',views.sp_delete,name='sp_delete'),		

	url(r'^st$',views.st,name='st'),	
	url(r'^st/update$',views.st_update,name='st_update'),	
	url(r'^st/delete/(\d+)/$',views.st_delete,name='st_delete'),		

	url(r'^ge$',views.ge,name='ge'),	
	url(r'^ge/update$',views.ge_update,name='ge_update'),	
	url(r'^ge/delete/(\d+)/$',views.ge_delete,name='ge_delete'),		

	url(r'^gr$',views.gr,name='gr'),	
	url(r'^gr/update$',views.gr_update,name='gr_update'),	
	url(r'^gr/delete/(\d+)/$',views.gr_delete,name='gr_delete'),		

	url(r'^cr$',views.cr,name='cr'),	
	url(r'^cr/update$',views.cr_update,name='cr_update'),	
	url(r'^cr/delete/(\d+)/$',views.cr_delete,name='cr_delete'),		

	url(r'^ii$',views.ii,name='ii'),	
	url(r'^ii/update$',views.ii_update,name='ii_update'),	
	url(r'^ii/delete/(\d+)/$',views.ii_delete,name='ii_delete'),		

	url(r'^dip$',views.dip,name='dip'),	
	url(r'^dip/update$',views.dip_update,name='dip_update'),	
	url(r'^dip/delete/(\d+)/$',views.dip_delete,name='dip_delete'),	

	url(r'^sd$',views.sd,name='sd'),	
	url(r'^sd/update$',views.sd_update,name='sd_update'),	
	url(r'^sd/delete/(\d+)/$',views.sd_delete,name='sd_delete'),	

	url(r'^ni$',views.ni,name='ni'),	
	url(r'^ni/update$',views.ni_update,name='ni_update'),	
	url(r'^ni/delete/(\d+)/$',views.ni_delete,name='ni_delete'),	

	url(r'^g1$',views.g1,name='g1'),	
	url(r'^g1/update$',views.g1_update,name='g1_update'),	
	url(r'^g1/delete/(\d+)/$',views.g1_delete,name='g1_delete'),	

	url(r'^g2$',views.g2,name='g2'),	
	url(r'^g2/update$',views.g2_update,name='g2_update'),	
	url(r'^g2/delete/(\d+)/$',views.g2_delete,name='g2_delete'),	

	url(r'^g3$',views.g3,name='g3'),	
	url(r'^g3/update$',views.g3_update,name='g3_update'),	
	url(r'^g3/delete/(\d+)/$',views.g3_delete,name='g3_delete'),	

	url(r'^g4$',views.g4,name='g4'),	
	url(r'^g4/update$',views.g4_update,name='g4_update'),	
	url(r'^g4/delete/(\d+)/$',views.g4_delete,name='g4_delete'),	

	url(r'^g5$',views.g5,name='g5'),	
	url(r'^g5/update$',views.g5_update,name='g5_update'),	
	url(r'^g5/delete/(\d+)/$',views.g5_delete,name='g5_delete'),	

	url(r'^g6$',views.g6,name='g6'),	
	url(r'^g6/update$',views.g6_update,name='g6_update'),	
	url(r'^g6/delete/(\d+)/$',views.g6_delete,name='g6_delete'),	
]

