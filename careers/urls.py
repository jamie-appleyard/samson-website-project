from django.urls import path
from .views import apply_view, careers_page

urlpatterns = [
    path('', careers_page, name='careers'),
    path('<int:pk>/', apply_view, name='apply'),
]