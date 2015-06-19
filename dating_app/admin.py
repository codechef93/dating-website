from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'gender', 'age', 'interests', 'photo')
    ordering = ['user']


admin.site.register(Profile, ProfileAdmin)
