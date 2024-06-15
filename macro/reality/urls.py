# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('templates/base', views.base, name='base'),
    path('templates/index', views.index, name='index'),  # Define the index view
    path('templates/email/', views.my_email_template_view, name='email'),
    path('templates/reg/', views.register, name='register'),
    path('success/', views.success, name='success'),  # Define a success view
]

