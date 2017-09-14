# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20170707_1753'),
        ('goods', '0002_auto_20170711_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartsGoods',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('cgoods', models.ForeignKey(to='goods.GoodsInfo')),
                ('cuser', models.ForeignKey(to='user.UserInfo')),
            ],
        ),
    ]
