# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('templates/email/', views.my_email_template_view, name='email'),
]