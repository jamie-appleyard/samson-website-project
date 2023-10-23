from django.urls import path
from news.views import news_view, article_view, load_articles

urlpatterns = [
    path('', news_view, name='news'),
    path('<int:pk>', article_view, name="article"),
    path('load-articles', load_articles, name="load_articles"),
    ]