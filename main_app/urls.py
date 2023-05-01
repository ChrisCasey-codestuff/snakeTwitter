
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('accounts/signup/', views.signup, name='signup'),

  path('tweets/feed/', views.feed, name='feed'),

  path('tweets/create_tweet/', views.create_tweet, name='create_tweet'),

  path('accounts/create_profile/', views.create_profile, name='create_profile'),

  path('users/<username>/', views.user_detail, name='user_detail'),

  path('tweets/user/feed/', views.userFeed, name='user_feed'),

  path('tweets/<int:id>/delete/', views.delete_tweet, name='delete_tweet'),

  path('tweets/<int:tweet_id>/like/', views.add_like, name='add_like'),

  path('tweets/<int:tweet_id>/retweet/', views.retweet, name='retweet'),

 # path('signup/', views.signup, name='signup'),
 ## path('tweets/delete_tweet', views.delete_tweet, name='create_tweet'),

 ## path('tweets/edit_tweet', views.edit_tweet, name='create_tweet'),
]