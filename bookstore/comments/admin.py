from django.contrib import admin

# Register your models here.
from comments.models import Comments
admin.site.register(Comments)