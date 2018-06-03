# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-03 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20180603_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='crop_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI_INFO_ID', models.IntegerField()),
                ('CI_VEGETABLES', models.CharField(max_length=100)),
                ('CI_NG_SEEDING_VAR', models.CharField(max_length=100)),
                ('CI_SCION_VAR', models.CharField(max_length=100)),
                ('CI_INFO_GATHER', models.IntegerField()),
                ('CI_GATHER_CODE', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='dip_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DIP_ID', models.IntegerField()),
                ('D_ID', models.CharField(max_length=100)),
                ('I_ID', models.CharField(max_length=100)),
                ('P_ID', models.CharField(max_length=100)),
                ('CI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.crop_info')),
            ],
        ),
        migrations.CreateModel(
            name='germination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GE_ID', models.IntegerField()),
                ('GE_RATE', models.FloatField()),
                ('GE_ENERGY', models.FloatField()),
                ('GE_DAYS', models.FloatField()),
                ('GE_UNIFORMITY', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='grafting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GR_ID', models.IntegerField()),
                ('GR_TAKE_RATE', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='image_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMI_ID', models.IntegerField()),
                ('IMI_DEVICE_CODE', models.IntegerField()),
                ('IMI_SNAP_DATE', models.DateField()),
                ('IMI_RESOLUTION', models.IntegerField()),
                ('IMI_IPIAI', models.CharField(max_length=255)),
                ('IMI_RAW_DATA', models.CharField(max_length=255)),
                ('CI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.crop_info')),
            ],
        ),
        migrations.CreateModel(
            name='nursery_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NI_SEDDING_ID', models.IntegerField()),
                ('NI_PH', models.FloatField()),
                ('NI_LN', models.FloatField()),
                ('NI_LL', models.FloatField()),
                ('NI_LW', models.FloatField()),
                ('NI_HL', models.FloatField()),
                ('NI_HSD', models.FloatField()),
                ('NI_SDGP', models.FloatField()),
                ('NI_SDA', models.FloatField()),
                ('NI_FBN', models.IntegerField()),
                ('NI_FFN', models.IntegerField()),
                ('NI_PFW', models.FloatField()),
                ('NI_SFW', models.FloatField()),
                ('NI_LFW', models.FloatField()),
                ('NI_S_FRESH_W', models.FloatField()),
                ('NI_ROOT_FW', models.FloatField()),
                ('NI_PDW', models.FloatField()),
                ('NI_SDW', models.FloatField()),
                ('NI_L_DRY_W', models.FloatField()),
                ('NI_S_DRY_W', models.FloatField()),
                ('NI_ROOT_DRY_W', models.FloatField()),
                ('NI_SRR', models.FloatField()),
                ('NI_SC', models.FloatField()),
                ('NI_LA', models.FloatField()),
                ('NI_LAI', models.FloatField()),
                ('NI_LAR', models.FloatField()),
                ('NI_SLA', models.FloatField()),
                ('NI_LI', models.FloatField()),
                ('NI_LIE', models.FloatField()),
                ('NI_LIC', models.FloatField()),
                ('NI_REC', models.FloatField()),
                ('NI_RUE', models.FloatField()),
                ('NI_NPR', models.FloatField()),
                ('NI_STOMATAL_C', models.FloatField()),
                ('NI_TR', models.FloatField()),
                ('NI_CGR', models.FloatField()),
                ('NI_RGR', models.FloatField()),
                ('NI_LEAF_TEMP', models.FloatField()),
                ('NI_CC', models.FloatField()),
                ('NI_PWC', models.FloatField()),
                ('NI_IA', models.FloatField()),
                ('NI_APF', models.FloatField()),
                ('CI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.crop_info')),
            ],
        ),
        migrations.CreateModel(
            name='plan_stages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PS_PLAN_CODE', models.IntegerField()),
                ('FI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.e1model')),
                ('GI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.gb_info')),
            ],
        ),
        migrations.CreateModel(
            name='seedling_date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SD_PROCESS_ID', models.IntegerField()),
                ('SD_START_DATE', models.DateField()),
                ('SD_END_DATE', models.DateField()),
                ('CI_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.crop_info')),
                ('PS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.plan_stages')),
            ],
        ),
        migrations.CreateModel(
            name='seedling_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SP_ID', models.IntegerField()),
                ('SP_DATE', models.DateField()),
                ('SP_TRAY', models.IntegerField()),
                ('SP_GROW_MEDIA', models.CharField(max_length=50)),
                ('SP_PRODUCTION', models.IntegerField()),
                ('SP_SEEDING_DATE', models.DateField()),
                ('SP_GRAFTING_DATE', models.DateField()),
                ('SP_SCION_GRAFT', models.IntegerField()),
                ('SP_ROOT_GRAFT', models.IntegerField()),
                ('SP_GRAFT_TAKE', models.IntegerField()),
                ('SP_SHIPPING_DATE', models.DateField()),
                ('PS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.plan_stages')),
            ],
        ),
        migrations.CreateModel(
            name='storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ST_STORAGE_ID', models.IntegerField()),
                ('ST_TEMP', models.FloatField()),
                ('ST_PERIOD', models.IntegerField()),
                ('ST_QUALITY', models.CharField(max_length=100)),
                ('ST_RESP_COEF', models.IntegerField()),
                ('ST_RESP_RATE', models.IntegerField()),
                ('ST_RESP_LOSS', models.FloatField()),
                ('ST_SURV_RATE', models.FloatField()),
                ('PS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.plan_stages')),
            ],
        ),
        migrations.AddField(
            model_name='grafting',
            name='PS_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.plan_stages'),
        ),
        migrations.AddField(
            model_name='germination',
            name='PS_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.plan_stages'),
        ),
    ]
