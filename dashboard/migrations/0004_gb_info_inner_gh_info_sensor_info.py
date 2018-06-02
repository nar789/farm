# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_device_admin_device_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='gb_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GB_NUMBER', models.IntegerField(null=True)),
                ('GB_KIND_CODE', models.CharField(max_length=20)),
                ('GB_FA_LATITUDE', models.FloatField(null=True)),
                ('GB_FA_LONGITUDE', models.FloatField(null=True)),
                ('GB_SIZE', models.FloatField(null=True)),
                ('GB_ARCHITECTURE', models.CharField(max_length=50)),
                ('GB_CONT_KIND', models.CharField(max_length=50)),
                ('GB_INSTALL_DIAGRM', models.CharField(max_length=50)),
                ('GB_DIGITAL_MANUAL', models.CharField(max_length=50)),
                ('GB_FA_LAND_CATER', models.CharField(max_length=50)),
                ('GB_CENTER_DIRECT', models.CharField(max_length=10)),
                ('GB_INSTAL', models.CharField(max_length=50)),
                ('GB_MANUFA', models.CharField(max_length=50)),
                ('GB_MAINTE_COMP', models.CharField(max_length=50)),
                ('DA_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.device_admin')),
                ('FI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.e1model')),
            ],
        ),
        migrations.CreateModel(
            name='inner_gh_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GB_DONG_NUMBER', models.IntegerField(null=True)),
                ('GB_KIND_CROP', models.CharField(max_length=50)),
                ('GB_INNER_SIZE', models.IntegerField(null=True)),
                ('GB_INNER_KIND', models.CharField(max_length=10)),
                ('GB_INNER_DEVI_LOC', models.IntegerField(null=True)),
                ('GB_INFO_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.gb_info')),
            ],
        ),
        migrations.CreateModel(
            name='sensor_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SI_ID', models.IntegerField(null=True)),
                ('SI_KIND', models.CharField(max_length=10)),
                ('SI_ACTU_CODE', models.CharField(max_length=2)),
                ('CI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.com_infor')),
                ('DC_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.device_code')),
                ('IGI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.inner_gh_info')),
            ],
        ),
    ]