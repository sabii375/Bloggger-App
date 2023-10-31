from django.contrib import admin
from .models import UserTable,Blog,Login,Category

# Register your models here.

admin.site.register(UserTable)
admin.site.register(Category)
admin.site.register(Blog)