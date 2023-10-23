from django.urls import path, re_path
from django.conf.urls import url
from .views import SignUpView, activate

urlpatterns = [
    # path('signup/', SignUpView, name='signup'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$', activate, name='activate'),
]