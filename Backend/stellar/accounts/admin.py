# Register your models here.
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.models import User

# Optionally, you can customize the UserAdmin class
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Register User with Django's default UserAdmin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Add custom configuration if needed
    # For example, to show specific fields in the list view:
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)
