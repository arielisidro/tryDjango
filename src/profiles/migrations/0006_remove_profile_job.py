# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20150926_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
    ]
