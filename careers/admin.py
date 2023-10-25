from django.contrib import admin
from .models import Career, JobApplication, TrainingInterest

class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email_address',
        'mobile_number',
        'first_line',
        'second_line',
        'town',
        'county',
        'postcode',
        'uk_bank_account',
        'criminal_offences',
        'over_18',
        'job_reference',
        'address_history',
        'sia_badge',
        'sia_badges',
        'working_history',
        'right_to_work',
        'group_a',
        'group_b',
        'cv',
        "result",
    )

class CareersAdmin(admin.ModelAdmin):
    list_display = (
        "job_title",
        "job_summary",
        "job_description",
        "rate_of_pay", 
        "job_location",
        "job_number_of_positions",
        "job_date_posted",
        "job_posted_by",
        "job_apply_by_date",
        "job_average_weekly_hours",
        "job_contract_type",
        "job_type",
        "vetting_required",
        "number_of_applications",
        )

class TrainingInterestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'course'
    )

admin.site.register(Career, CareersAdmin)
admin.site.register(JobApplication, ApplicationAdmin)
admin.site.register(TrainingInterest, TrainingInterestAdmin)

