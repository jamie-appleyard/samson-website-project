from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=12, blank=False)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return (self.email)


class UserType(models.Model):
    class UserTypes(models.IntegerChoices):
        APPLICANT = 0, 'Applicant'
        INTERVIEWEE = 1, 'Interviewee'
        STAFF = 2, 'Staff'
        RESERVE = 3, 'Reserve'
        MANAGEMENT = 4, 'Management'
        DIRECTOR = 5, 'Director'

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    user_type = models.SmallIntegerField(
        choices=UserTypes.choices,
        default=UserTypes.APPLICANT,
    )

    def __str__(self):
        return (self.user.email)


class VettingStatus(models.Model):
    class VettingTypes(models.IntegerChoices):
        NOT_VETTED = 0, 'Not Vetted'
        FORM_SENT = 1, 'Form Sent'
        FORM_SUBMITTED = 2, 'Form Submitted'
        IN_PROGRESS = 3, 'In Progress'
        LIMITED_VETTING = 4, 'Limited Vetting'
        FULLY_VETTED = 5, 'Fully Vetted'
        NOT_REQUIRED = 6, "Not Required"
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='vetting_status')
    vetting_status = models.SmallIntegerField(
        choices=VettingTypes.choices,
        default=VettingTypes.NOT_VETTED,
    )

    def __str__(self):
        return (self.user.email)