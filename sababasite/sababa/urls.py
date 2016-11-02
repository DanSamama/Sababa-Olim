from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/login$', 'django.contrib.auth.views.login'),
    url(r'^sababa/$', views.home, name='home'),
]
