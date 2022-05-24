from django.contrib import admin

# Register your models here.

from authorization.models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    ordering = ['username']
    search_fields = ['username', 'email']
    list_filter = ['username']


admin.site.register(Profile)