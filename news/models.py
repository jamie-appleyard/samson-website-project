from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=55, blank=True)
    heading = models.CharField(max_length=200, blank=True)
    sub_heading = models.CharField(max_length=500, blank=True)
    image_main = models.ImageField(upload_to='news/', blank=True)
    text = models.TextField(max_length=3000, blank=True)
    author = models.CharField(max_length=200, blank=True)
    featured = models.BooleanField(default=False)

    class Status(models.IntegerChoices):
        LIVE = 0, 'Live'
        DRAFT = 1, 'Draft'
        DELETED = 2, 'Deleted'
    
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    date_posted = models.DateField(auto_now_add=True)
    date_last_modified = models.DateField(auto_now=True)
