from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, UserType, VettingStatus

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'id','username','first_name','last_name',
        'date_joined','email','mobile_number',
        'is_staff','is_active', 'email_verified',
        ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('mobile_number', 'email_verified')}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('mobile_number','email_verified')}),
    )

class UserTypeAdmin(admin.ModelAdmin):
    model = UserType
    list_display = [
        'user', 'user_type'
    ]

class VettingStatusAdmin(admin.ModelAdmin):
    model = VettingStatus
    list_display = [
        'user', 'vetting_status'
    ]



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(VettingStatus, VettingStatusAdmin)
