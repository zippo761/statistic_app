from django.contrib import admin

from .models import UserProfile
from .models import User


class AccountAdmin(admin.ModelAdmin):
    """Admin table setting"""
    # what we will see in admin table
    list_display = ['id', 
                    'user', 
                    'description',
                    'location',
                    'date_joined',
                    'simple_user']

    # link for name of user account and id      
    list_display_links = ('id', 'user')

    # field for search in admin
    search_fields = ['user', 'date_joined']



admin.site.register(UserProfile, AccountAdmin)
