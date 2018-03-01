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
