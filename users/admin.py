from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    fields = ['username', 'password', 'is_superuser',
              'is_staff', 'is_active']
