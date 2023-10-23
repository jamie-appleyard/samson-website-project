from django.contrib import admin
from .models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'contact_number',
        'email',
        'message',
    ]

admin.site.register(Enquiry, EnquiryAdmin)