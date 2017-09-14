# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170707_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeinfo',
            old_name='ttile',
            new_name='ttitle',
        ),
    ]
