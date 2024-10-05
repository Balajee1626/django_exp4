# your_app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send_email/', views.send_email, name='send_email'),
]
