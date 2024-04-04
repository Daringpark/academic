from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Store, Product
from accounts.models import User 

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Store)
admin.site.register(Product)