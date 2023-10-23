from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=1000, help_text="Hello Samson ...")