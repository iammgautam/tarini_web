from django.urls import path
from tarini_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('sms_sent/', views.sms_sent, name='sms_sent')
]