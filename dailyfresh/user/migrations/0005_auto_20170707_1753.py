# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170707_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gtype',
        ),
        migrations.DeleteModel(
            name='GoodsInfo',
        ),
        migrations.DeleteModel(
            name='TypeInfo',
        ),
    ]
