from django.urls import path
from .views import dashboard_view, vacancy_tab, news_editor, news_room, news_update, enquiries_view, applications_view, applicant_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('vacancy', vacancy_tab, name='vacancy'),
    path('applications/<int:pk>', applications_view, name='applications'),
    path('applicant/<int:pk>', applicant_view, name='applicant'),
    path('editor', news_editor, name='editor'),
    path('update/<int:pk>', news_update, name='update'),
    path('newsroom', news_room, name="news_room"),
    path('enquiries', enquiries_view, name='enquiries'),
]