from django.urls import path
from login import views

urlpatterns = [
    path('', views.index, name='indexxx'),
    path('login/', views.login, name='loginnn'),
    path('register/', views.register, name='registerrr'),
]