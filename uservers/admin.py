from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post

# Register your models here.


class myUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class myPostAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'updated_at')
    search_fields = ('text',)
    ordering = ('created_at', 'updated_at')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, myUserAdmin)
admin.site.register(Post, myPostAdmin)