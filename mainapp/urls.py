# chat/urls.py
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.page, name='index'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^login/$', login, name='login'),  # The base django login view
    url(r'^logout/$', logout, name='logout'),  # The base django logout view
]