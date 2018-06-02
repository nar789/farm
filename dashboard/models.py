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


class inner_gh_info(models.Model):
	GB_DONG_NUMBER=models.IntegerField(null=True)
	GB_INFO_ID=models.ForeignKey(gb_info)
	GB_KIND_CROP=models.CharField(max_length=50)
	GB_INNER_SIZE=models.IntegerField(null=True)
	GB_INNER_KIND=models.CharField(max_length=10)
	GB_INNER_DEVI_LOC=models.IntegerField(null=True)

	def __str__(self):
		return "inner_gh_info#%s" % self.id

class sensor_info(models.Model):
	SI_ID=models.IntegerField(null=True)
	SI_KIND=models.CharField(max_length=10)
	SI_ACTU_CODE=models.CharField(max_length=2)
	DC_ID=models.ForeignKey(device_code)
	CI_ID=models.ForeignKey(com_infor)
	IGI_ID=models.ForeignKey(inner_gh_info)

	def __str__(self):
		return "sensor_info$%s" % self.id