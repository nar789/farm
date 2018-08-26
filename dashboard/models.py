# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class e1model(models.Model):
	GB_FA_ID=models.CharField(max_length=30)
	GB_FA_PW=models.CharField(max_length=20)
	CTVT_FCLTY_ID=models.CharField(max_length=30)
	GB_FA_PHONE=models.CharField(max_length=13)
	GB_FA_EMAIL=models.CharField(max_length=30)
	GB_FA_ADDR=models.CharField(max_length=100)
	GB_FA_NAME=models.CharField(max_length=20)
	GB_FA_SIZE=models.IntegerField(null=True)
	GB_FAM_NUM=models.IntegerField(null=True)
	GB_COOPER_UNIT=models.CharField(max_length=30)

	def __str__(self):
		return "e1#%s" % self.id


class com_infor(models.Model):
	CI_CODE=models.CharField(max_length=10)
	CI_NAME=models.CharField(max_length=30)
	CI_ADDR=models.CharField(max_length=100)
	CI_PHONE=models.CharField(max_length=13)

	def __str__(self):
		return "com_infor#%s" % self.id

class device_code(models.Model):
	DC_CODE=models.CharField(max_length=10)
	DC_KIND=models.CharField(max_length=20)

	def __str__(self):
		return "device_code#%s" % self.id

class device_admin(models.Model):
	DA_ID=models.CharField(max_length=10)
	DA_NAME=models.CharField(max_length=20)
	DA_PHONE=models.CharField(max_length=13)
	DA_ROLE=models.CharField(max_length=20)
	CI_ID=models.ForeignKey(com_infor)

	def __str__(self):
		return "device_admin#%s" % self.id

class gb_info(models.Model):
	FI_ID=models.ForeignKey(e1model)
	GB_NUMBER=models.IntegerField(null=True)
	GB_KIND_CODE=models.CharField(max_length=20)
	GB_FA_LATITUDE=models.FloatField(null=True)
	GB_FA_LONGITUDE=models.FloatField(null=True)
	GB_SIZE=models.FloatField(null=True)
	GB_ARCHITECTURE=models.CharField(max_length=50)
	GB_CONT_KIND=models.CharField(max_length=50)
	GB_INSTALL_DIAGRM=models.CharField(max_length=50)
	GB_DIGITAL_MANUAL=models.CharField(max_length=50)
	GB_FA_LAND_CATER=models.CharField(max_length=50)
	GB_CENTER_DIRECT=models.CharField(max_length=10)
	GB_INSTAL=models.CharField(max_length=50)
	GB_MANUFA=models.CharField(max_length=50)
	GB_MAINTE_COMP=models.CharField(max_length=50)
	DA_ID=models.ForeignKey(device_admin)

	def __str__(self):
		return "gb_info#%s" % self.id

class sensor_info(models.Model):
	SI_ID=models.IntegerField(null=True)
	SI_KIND=models.CharField(max_length=10)
	SI_ACTU_CODE=models.CharField(max_length=2)
	DC_ID=models.ForeignKey(device_code)
	CI_ID=models.ForeignKey(com_infor)

	def __str__(self):
		return "sensor_info$%s" % self.id

class inner_gh_info(models.Model):
	GB_DONG_NUMBER=models.IntegerField(null=True)
	GB_INFO_ID=models.ForeignKey(gb_info)
	GB_KIND_CROP=models.CharField(max_length=50)
	GB_INNER_SIZE=models.IntegerField(null=True)
	GB_INNER_KIND=models.CharField(max_length=10)
	GB_INNER_DEVI_LOC=models.IntegerField(null=True)
	GB_DEVICE_ID=models.ForeignKey(sensor_info)

	def __str__(self):
		return "inner_gh_info#%s" % self.id

class work_info(models.Model):
	GM_WORK_ID=models.IntegerField(null=True)
	GM_WORK_DATE=models.DateField(auto_now=False)
	GM_WORK_LINE_NUM=models.IntegerField(null=True)
	GM_LABOR_TIME=models.TimeField(auto_now=False)
	GM_WORK_INFO=models.CharField(max_length=50)
	GM_AGRI_MTRI_IN_WORK=models.CharField(max_length=50)
	GM_WORK_CODE=models.CharField(max_length=5)
	GM_WORK_OP=models.CharField(max_length=50)
	FI_ID=models.ForeignKey(e1model)
	CI_ID=models.ForeignKey(gb_info)

	def __str__(self):
		return "work_info#%s" % self.id


class mainte_info(models.Model):
	WI_ID=models.ForeignKey(work_info)
	GM_MAINTE_WORKE_DATE=models.DateTimeField(auto_now=False)
	GM_FACITY_NAME=models.CharField(max_length=50)
	GM_MAINTE_INFO=models.CharField(max_length=50)
	GM_REPAIR_COST=models.IntegerField(null=True)

	def __str__(self):
		return "mainte_info#%s" % self.id

class harves_info(models.Model):
	GM_HARVES_ID=models.IntegerField(null=True)
	GM_DATE_HARVES=models.DateTimeField(auto_now=False)
	GM_HARVES_YIELD=models.FloatField(null=True)
	GM_WEIGHT=models.FloatField(null=True)
	GM_QUALIT_GRAD=models.CharField(max_length=10)
	WI_ID=models.ForeignKey(work_info)

	def __str__(self):
		return "harves_info#%s" % self.id

class after_harves_info(models.Model):
	GM_LOT_NUM=models.IntegerField(null=True)
	GM_INFO_PROCESS=models.CharField(max_length=50)
	HI_ID=models.ForeignKey(harves_info)

	def __str__(self):
		return "after_harves_info#%s" % self.id

class sale_info(models.Model):
	GM_SALE_ID=models.IntegerField(null=True)
	GM_SALE_DATE=models.DateField(auto_now=False)
	GM_METHODS_SALE=models.CharField(max_length=30)
	GM_PACK_UNIT=models.CharField(max_length=5)
	GM_GALSE=models.FloatField(null=False)
	GM_PRICE_BOX=models.IntegerField(null=False)
	GM_TOTAL_INCOME=models.IntegerField(null=False)
	HI_ID=models.ForeignKey(harves_info)

	def __str__(self):
		return "sale_info#%s" % self.id

class plan_stages(models.Model):
	PS_PLAN_CODE=models.IntegerField(null=False)
	
	def __str__(self):
		return "plan_stages#%s" % self.id

class crop_info(models.Model):
	CI_INFO_ID=models.IntegerField(null=False)
	CI_VEGETABLES=models.CharField(max_length=100)
	CI_NG_SEEDING_VAR=models.CharField(max_length=100)
	CI_SCION_VAR=models.CharField(max_length=100)
	CI_INFO_GATHER=models.IntegerField(null=False)
	CI_GATHER_CODE=models.IntegerField(null=False)
	GB_INNER_FA_ID=models.ForeignKey(inner_gh_info)

	def __str__(self):
		return "crop_info#%s" % self.id


class seedling_plan(models.Model):
	SP_ID=models.IntegerField(null=False)
	SP_DATE=models.DateField(auto_now=False)
	SP_TRAY=models.IntegerField(null=False)
	SP_GROW_MEDIA=models.CharField(max_length=50)
	SP_PRODUCTION=models.IntegerField(null=False)
	SP_SEEDING_DATE=models.DateField(auto_now=False)
	SP_GRAFTING_DATE=models.DateField(auto_now=False)
	SP_SCION_GRAFT=models.IntegerField(null=False)
	SP_ROOT_GRAFT=models.IntegerField(null=False)
	SP_GRAFT_TAKE=models.IntegerField(null=False)
	SP_SHIPPING_DATE=models.DateField(auto_now=False)
	PS_ID=models.ForeignKey(plan_stages)
	CI_INFO_ID=models.ForeignKey(crop_info)

	def __str__(self):
		return "seedling_plan#%s" % self.id

class storage(models.Model):
	ST_STORAGE_ID=models.IntegerField(null=False)
	ST_TEMP=models.FloatField(null=False)
	ST_PERIOD=models.IntegerField(null=False)
	ST_QUALITY=models.CharField(max_length=100)
	ST_RESP_COEF=models.IntegerField(null=False)
	ST_RESP_RATE=models.IntegerField(null=False)
	ST_RESP_LOSS=models.FloatField(null=False)
	ST_SURV_RATE=models.FloatField(null=False)
	PS_ID=models.ForeignKey(plan_stages)

	def __str__(self):
		return "storage#%s" % self.id

class germination(models.Model):
	GE_ID=models.IntegerField(null=False)
	GE_RATE=models.FloatField(null=False)
	GE_ENERGY=models.FloatField(null=False)
	GE_DAYS=models.FloatField(null=False)
	GE_UNIFORMITY=models.FloatField(null=False)
	PS_ID=models.ForeignKey(plan_stages)

	def __str__(self):
		return "germination#%s" % self.id

class grafting(models.Model):
	GR_ID=models.IntegerField(null=False)
	GR_TAKE_RATE=models.FloatField(null=False)
	PS_ID=models.ForeignKey(plan_stages)

	def __str__(self):
		return "grafting#%s" % self.id



class image_info(models.Model):
	IMI_ID=models.IntegerField(null=False)
	IMI_DEVICE_CODE=models.IntegerField(null=False)
	IMI_SNAP_DATE=models.DateField(auto_now=False)
	IMI_RESOLUTION=models.IntegerField(null=False)
	IMI_IPIAI=models.CharField(max_length=255)
	IMI_RAW_DATA=models.CharField(max_length=255)
	CI_ID=models.ForeignKey(crop_info)

	def __str__(self):
		return "image_info#%s" % self.id


class dip_info(models.Model):
	DIP_ID=models.IntegerField(null=False)
	D_ID=models.CharField(max_length=100)
	I_ID=models.CharField(max_length=100)
	P_ID=models.CharField(max_length=100)
	CI_ID=models.ForeignKey(crop_info)

	def __str__(self):
		return "dip_info#%s" % self.id

class nursery_info(models.Model):
	NI_SEDDING_ID=models.IntegerField(null=False)
	NI_PH=models.FloatField(null=False)
	NI_LN=models.FloatField(null=False)
	NI_LL=models.FloatField(null=False)
	NI_LW=models.FloatField(null=False)
	NI_HL=models.FloatField(null=False)
	NI_HSD=models.FloatField(null=False)
	NI_SDGP=models.FloatField(null=False)
	NI_SDA=models.FloatField(null=False)
	NI_FBN=models.IntegerField(null=False)
	NI_FFN=models.IntegerField(null=False)
	NI_PFW=models.FloatField(null=False)
	NI_SFW=models.FloatField(null=False)
	NI_LFW=models.FloatField(null=False)
	NI_S_FRESH_W=models.FloatField(null=False)
	NI_ROOT_FW=models.FloatField(null=False)
	NI_PDW=models.FloatField(null=False)
	NI_SDW=models.FloatField(null=False)
	NI_L_DRY_W=models.FloatField(null=False)
	NI_S_DRY_W=models.FloatField(null=False)
	NI_ROOT_DRY_W=models.FloatField(null=False)
	NI_SRR=models.FloatField(null=False)
	NI_SC=models.FloatField(null=False)
	NI_LA=models.FloatField(null=False)
	NI_LAI=models.FloatField(null=False)
	NI_LAR=models.FloatField(null=False)
	NI_SLA=models.FloatField(null=False)
	NI_LI=models.FloatField(null=False)
	NI_LIE=models.FloatField(null=False)
	NI_LIC=models.FloatField(null=False)
	NI_REC=models.FloatField(null=False)
	NI_RUE=models.FloatField(null=False)
	NI_NPR=models.FloatField(null=False)
	NI_STOMATAL_C=models.FloatField(null=False)
	NI_TR=models.FloatField(null=False)
	NI_CGR=models.FloatField(null=False)
	NI_RGR=models.FloatField(null=False)
	NI_LEAF_TEMP=models.FloatField(null=False)
	NI_CC=models.FloatField(null=False)
	NI_PWC=models.FloatField(null=False)
	NI_IA=models.FloatField(null=False)
	NI_APF=models.FloatField(null=False)
	CI_ID=models.ForeignKey(crop_info)

	def __str__(self):
		return "nursery_info#%s" % self.id

class seedling_date(models.Model):
	SD_PROCESS_ID=models.IntegerField(null=False)
	SD_START_DATE=models.DateField(auto_now=False)
	SD_END_DATE=models.DateField(auto_now=False)
	PS_ID=models.ForeignKey(plan_stages)
	CI_ID=models.ForeignKey(crop_info)

	def __str__(self):
		return "seedling_date#%s" % self.id

class nutrient_state(models.Model):
	GB_INNER_FA_ID=models.ForeignKey(gb_info)
	GE_SUPPLY_START_TIME=models.TimeField(auto_now=False)
	GE_SUPPLY_END_TIME=models.TimeField(auto_now=False)
	GE_WATER_OUT=models.FloatField(null=False)
	GE_SUPPLY_EC=models.FloatField(null=False)
	GE_SUPPLY_PH=models.FloatField(null=False)
	GE_SPLY_CONST_CONCEN=models.FloatField(null=False)
	GE_FLOW_OUT=models.FloatField(null=False)
	GE_DRAIN_EC=models.FloatField(null=False)
	GE_DRAIN_PH=models.FloatField(null=False)
	GE_DRAIN_CONST_CONCEN=models.FloatField(null=False)

	def __str__(self):
		return "nutrient_state#%s" % self.id

class onoff_act(models.Model):
	GB_INNER_FA_ID=models.ForeignKey(gb_info)
	GB_EVENT_TIME=models.TimeField(auto_now=False)
	GE_FAN=models.NullBooleanField()
	GE_SUPPORT_LIGHT=models.NullBooleanField()
	GE_HEAT=models.NullBooleanField()
	GE_IRRIGA=models.NullBooleanField()
	GE_CO2_GE=models.NullBooleanField()
	GE_FOG=models.NullBooleanField()

	def __str__(self):
		return "onoff_act#%s" % self.id

class actuator(models.Model):
	GB_INNER_FA_ID=models.ForeignKey(gb_info)
	GE_ACTION_TIME=models.TimeField(auto_now=False)
	GE_TOP_VENT=models.NullBooleanField()
	GE_SIDE_VENT=models.NullBooleanField()
	GE_HORIZN_CURTAN=models.NullBooleanField()
	GE_VERTICAL_CURTAN=models.NullBooleanField()

	def __str__(self):
		return "actuator#%s" % self.id

class env_root(models.Model):
	GB_INNER_FA_ID=models.ForeignKey(gb_info)
	GE_ROOT_TIME=models.TimeField(auto_now=False)
	GE_GROUND_TEMP=models.FloatField(null=False)
	GE_GROUND_HUMI=models.FloatField(null=False)
	GE_EC=models.FloatField(null=False)
	GE_PH=models.FloatField(null=False)

	def __str__(self):
		return "env_root#%s" % self.id

class env_outer(models.Model):
	GB_INNER_FA_ID=models.ForeignKey(gb_info)
	GB_OUT_TIME=models.TimeField(auto_now=False)
	GE_OUT_TEMP=models.FloatField(null=False)
	GE_OUT_HUMI=models.FloatField(null=False)
	GE_OUT_WIND_DIRECT=models.FloatField(null=False)
	GE_OUT_WIND_SPD=models.FloatField(null=False)
	GE_SOLAR_RADI=models.FloatField(null=False)
	GE_RAINF=models.FloatField(null=False)

	def __str__(self):
		return "env_outer#%s" % self.id

class env_inner(models.Model):
	GB_INNER_FA_ID=models.ForeignKey(gb_info)
	GE_IN_TIME=models.TimeField(auto_now=False)
	GE_IN_TEMP=models.FloatField(null=False)
	GE_IN_HUMI=models.FloatField(null=False)
	GE_IN_CO2=models.FloatField(null=False)
	GE_IN_SOLAR_RADI=models.FloatField(null=False)
	GE_IN_WIND_SPD=models.FloatField(null=False)

	def __str__(self):
		return "env_inner#%s" % self.id