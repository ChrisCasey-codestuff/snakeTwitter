
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('feed/', views.feed, name='feed'),

  path('user/<int:user_id>/', views.user_detail, name='user_detail'),
]