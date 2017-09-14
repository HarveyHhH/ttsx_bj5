# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userinfo_ucode'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=50)),
                ('gpic', models.ImageField(upload_to='')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gclick', models.IntegerField()),
                ('gunit', models.CharField(max_length=20)),
                ('gisdelte', models.BooleanField(default=False)),
                ('gsubtitle', models.CharField(max_length=200)),
                ('gstore', models.IntegerField()),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ttile', models.CharField(max_length=20)),
                ('tisdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='user.TypeInfo'),
        ),
    ]
