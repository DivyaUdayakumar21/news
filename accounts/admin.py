from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
        "occupation",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("age","occupation",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields" : ("age","occupation")}),)

admin.site.register(CustomUser, CustomUserAdmin)