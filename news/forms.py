from django import forms
from news.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['date_posted', 'date_last_modified', 'status']