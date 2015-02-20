# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('up', models.BigIntegerField()),
                ('down', models.BigIntegerField()),
                ('live_time', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
