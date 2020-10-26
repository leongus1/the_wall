from django.urls import path
from . import views

app_name = 'message_app'

urlpatterns = [
    path('/', views.index),
    path('/post_message/', views.post_message),
    path('/post_comment/', views.post_comment),
    path('/delete_message/<int:message_id>/', views.delete_message),
    path('/delete_comment/<int:comment_id>/', views.delete_comment),
]