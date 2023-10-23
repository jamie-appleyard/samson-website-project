from django.urls import path
from .views import (home_view, contact_view, solution_guarding, solution_monitoring, solution_engineering,
                    solution_key_management, solution_helpdesk, solution_professional, about_us, about_quality,
                    about_csr, about_accreditation)

urlpatterns = [
    #STATIC PAGES
    path('', home_view, name='home'),
    path('Contact', contact_view, name='contact'),
    path("about_us", about_us, name="about_us"),
    path("about_quality", about_quality, name="about_quality"),
    path("about_csr", about_csr, name="about_csr"),
    path("about_accreditation", about_accreditation, name="about_accreditation"),

    #SOLUTIONS
    path('Security-Guards', solution_guarding, name='s_guards'),
    path("Monitoring", solution_monitoring, name="s_monitoring"),
    path("Engineering", solution_engineering, name="s_engineering"),
    path("Key-Management", solution_key_management, name="s_keymanagement"),
    path("Help-Desk", solution_helpdesk, name="s_helpdesk"),
    path("Professional", solution_professional, name="s_professional"),
]