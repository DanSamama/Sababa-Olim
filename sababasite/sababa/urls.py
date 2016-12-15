from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^connect$', views.connect, name='connect'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^$', views.home, name='home'),
]
