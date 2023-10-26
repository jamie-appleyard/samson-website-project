from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

import datetime
from datetime import timedelta


#Model for the information behind a particular job listing
class Career(models.Model):
    job_title = models.CharField(max_length=200)
    job_summary = models.CharField(max_length=500)
    job_description = models.CharField(max_length=2000)
    rate_of_pay = models.DecimalField(max_digits=6, decimal_places=2)
    job_location = models.CharField(max_length=100)
    job_number_of_positions = models.IntegerField(MinValueValidator(1), default=1)
    TODAY = datetime.date.today()
    FORTNIGHT = timedelta(days=14)
    DEF_APPLY_DATE = (TODAY + FORTNIGHT).strftime("%d/%m/%y")
    TODAY_STRING = TODAY.strftime("%d/%m/%y")
    job_apply_by_date = models.CharField(max_length=12, default=DEF_APPLY_DATE)
    job_date_posted = models.CharField(max_length=12, default=TODAY_STRING, editable=False)
    job_posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    job_average_weekly_hours = models.IntegerField(default=45)

    CONTRACT_TYPE_CHOICES = [
        ('FT_T', 'Full time - Temporary'),
        ('FT_P', 'Full time - Permanent'),
        ('PT_T', 'Part time - Temporary'),
        ('PT_P', 'Part time - Permanent'),
    ]
    job_contract_type = models.CharField(
        max_length=30,
        choices = CONTRACT_TYPE_CHOICES,
        default = 'PT_T')

    JOB_TYPE_CHOICES = [
        ('REC', 'Receptionist'),
        ('SG', 'Security Guard'),
        ('RVRCOP', 'Control Room Operator'),
        ('CO','Cleaning Operative'),
        ('MD','Mobile Driver'),
        ('MS','Mobile Supervisor'),
        ('OPS','Operations Manager')
    ]
    job_type = models.CharField(
        max_length=30,
        choices = JOB_TYPE_CHOICES,
        default = 'SG')
    vetting_required = models.BooleanField(default=False)
    number_of_applications = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('vacancy')

#Model for the application form, collecting all applicant information (pre-vetting) for initial screening purposes.
class JobApplication(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=11)
    first_line = models.CharField(max_length=100, help_text="First Line of Address")
    second_line = models.CharField(max_length=100, blank=True, help_text="Second Line of Address")
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=7)
    uk_bank_account = models.BooleanField(default=False)
    criminal_offences = models.BooleanField(default=False)
    over_18 = models.BooleanField(default=False)
    job_reference = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='application')
    address_history = models.BooleanField(default=False)
    sia_badge = models.BooleanField(default=False)

    SIA_BADGE_TYPES = [
        ('DS', 'Door Supervisor'),
        ('CCTV', 'CCTV'),
        ('CP', 'Close Protection'),
        ('SG', 'Security Guarding'),
        ('VI', 'Vehicle Immobiliser'),
    ]

    sia_badges = MultiSelectField(
        max_length=100,
        choices=SIA_BADGE_TYPES,
        blank=True,
    )

    working_history = models.BooleanField(default=False)
    right_to_work = models.BooleanField(default=False)

    GROUP_A_CHOICES = [
        ('SVP', 'Signed Valid Passport'),
        ('UKBC', 'UK Birth Certificate'),
        ('UKDL', 'UK Driving License'),
        ('EUID', 'Valid EU ID Card'),
        ('UKFA', 'Valid UK Firearms License')
    ]
    group_a = MultiSelectField(
        max_length=300, 
        choices=GROUP_A_CHOICES,
        default='')

    GROUP_B_CHOICES = [
        ('MC', 'Marriage Certificate'),
        ('BNC', 'British National Certificate'),
        ('P45', 'P45**'),
        ('VBWP', 'Visa or British Work Certificate'),
        ('P60', 'P60**'),
        ('DWP', 'Letter from DWP'),
        ('BS', 'Bank Statement*'),
        ('CCS', 'Credit Card Statement*'),
        ('MS', 'Mortgage Statement**'),
        ('CS', 'Court Summons**'),
        ('UB', 'Utility Bill*'),
        ('CBL', 'Child Benefit Letter**'),
        ('TVL', 'TV License**'),
        ('PSAL', 'Pay Slip'),
        ('PS', 'Pension Statment'),
        ('CUKBC', 'Copy of UK Birth Certificate')
    ]
    group_b = MultiSelectField(
        max_length=300,
        choices=GROUP_B_CHOICES,
        default='')

    cv = models.FileField(upload_to='cv/', blank=True)

    class Result(models.IntegerChoices):
        UNDECIDED=0, 'Undecided'
        SUCCESS=1, 'Success'
        FAIL=2, 'Fail'
    result = models.SmallIntegerField(
        choices=Result.choices,
        default=Result.UNDECIDED,
    )

    def __str__(self):
        return str(self.id)

#Model to collect the data for those interested in taking training with us so that they can be contacted when appropriate
class TrainingInterest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    COURSE_CHOICES = [
        ("siatu", "SIA Top Up Training"),
        ("ds", "Door Supervisor Course"),
        ("first aid", "First Aid"),
        ("cctv", "CCTV Operator Course"),
        ("guarding", "Security Guarding Course"),
        ("cleaning", "BICS Cleaning Course"),
        ("reception", "Receptionist Practice and Professionalism"),
        ("ct", "Counter Terrorism")
    ]

    course = models.CharField(
        max_length=70,
        choices= COURSE_CHOICES,
        help_text = "Which course interests you most?"
        )

    def __str__(self):
        return str(self.email)



