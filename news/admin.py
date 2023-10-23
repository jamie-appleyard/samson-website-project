from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'heading',
        'sub_heading',
        'image_main',
        'text',
        'author',
        'featured',
        'status',
        'date_posted',
        'date_last_modified'
    ]

admin.site.register(Article, ArticleAdmin)