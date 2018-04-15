from django.db import models

class BaseModel(models.Model):
    '''模型抽象基类'''
    #我之后做的不同的应用模板里面都是继承的这个.
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True