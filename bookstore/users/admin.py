from django.contrib import admin

# Register your models here.
from users.models import Passport,Address

admin.site.register(Passport)
admin.site.register(Address)