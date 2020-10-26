from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register),
    path('register/success/', views.login),
    path('logged_out/', views.logout, name='logout'),
    path('check_log/', views.log_check),
]