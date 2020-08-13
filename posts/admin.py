from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from posts.models import Post
from django.contrib.auth.models import User
# Register your models here.

#admin.site.register(Profile)
@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'photo' )
    list_display_links = ('pk', 'user')
    list_editable = ('title',)
    search_fields = (
                    'user__email', 
                    'user__username', 
                    'user__first_name',
                    'user__last_name',
                    'phone_number')
    list_filter = (
                 'user__is_active',
                 'user__is_staff',
                 'created',
                 'modified',
                 )
