# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('disabled', models.BooleanField(verbose_name='禁用评论', default=False)),
                ('content', models.CharField(verbose_name='评论内容', max_length=1000)),
                ('book', models.ForeignKey(verbose_name='书籍ID', to='books.Books')),
                ('user', models.ForeignKey(verbose_name='用户ID', to='users.Passport')),
            ],
            options={
                'db_table': 's_comment_table',
            },
        ),
    ]
