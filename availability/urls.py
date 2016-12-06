from django.conf.urls import url
from availability import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^set/$', views.set_availability, name='set'),
    url(r'register/$', views.register_lecturer, name='register'),
    url(r'send-sms/$', views.notify_lecturers, name='notify_lecturers'),
    url(r'login/$', views.user_login, name='login'),
    url(r'logout/$', views.user_logout, name='logout'),
]