# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(verbose_name='商品图片', upload_to='books', storage=django.core.files.storage.FileSystemStorage(location='/root/bookstore/bookstore/collect_static')),
        ),
    ]
