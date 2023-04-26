
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('tweets/feed/', views.feed, name='feed'),

  path('user/<int:user_id>/', views.user_detail, name='user_detail'),

  path('tweets/create_tweet', views.create_tweet, name='create_tweet'),

 ## path('tweets/delete_tweet', views.delete_tweet, name='create_tweet'),

 ## path('tweets/edit_tweet', views.edit_tweet, name='create_tweet'),
]