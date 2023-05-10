from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User
from .models import Tweet
from .forms import TweetForm
from .forms import ProfileForm
from .models import Profile
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
import time
# Create your views here.
def home(request):
    return render(request, 'base.html')

def feed(request):
    tweetsList = Tweet.objects.all()
    form = TweetForm()
    return render(request, 'tweets/tweetsIndex.html',  { 'tweetsList': tweetsList, 'form': form})

def create_tweet (request):
    form = TweetForm(request.POST)
  # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
       new_tweet = form.save(commit=False)
       user = request.user
       new_tweet.date_time = datetime.datetime.now()
       #print(new_tweet)
       new_tweet.creator = (user)
       print(new_tweet.creator)
       new_tweet.save()
       return redirect('feed')

def userFeed(request):
    user = request.user
    profile = Profile.objects.get(user = request.user)

    user_retweet_set = user.tweet_set.all()
    user_tweets = Tweet.objects.filter(creator = user)
    print(user_retweet_set)
    form = TweetForm()


    return render(request, 'tweets/userTweets.html',  { 'userTweetsList': user_tweets, 'form': form, 'profile': profile, 'user_retweets': user_retweet_set})

def create_profile (request):
    #POST
    error_message = ''
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
          print('hello')
          new_profile = form.save(commit=False)
          new_profile.user = request.user
          new_profile.save()
          return redirect('feed')
    else:
        error_message = 'Invalid Inputs please try again'

    #GET

    form = ProfileForm()

    return render(request, 'registration/createProfile.html', {'form': form, 'error': error_message})

        #RENDER TEMPLATE



def signup (request):
    #POST
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          user = form.save()
          login(request, user)
          return redirect('create_profile')
    else:
        error_message = 'Invalid Inputs please try again'

    #GET

    form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form, 'error': error_message})
        #PROVIDE FORM
        #RENDER TEMPLATE

def user_detail(request, username):

    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    print(user)
    print(profile)
    user_retweet_set = user.tweet_set.all()
    user_tweets = Tweet.objects.filter(creator = user)
#create list of toys cat doesnt have
    print(user)
    return render(request, 'tweets/userDetailTweets.html', {'user_tweet_set': user_retweet_set, 'user': user, 'profile':profile, 'user_tweets':user_tweets})

def delete_tweet(request, id):
    tweet = Tweet.objects.get(id = id)
    tweet.delete()
    return redirect('feed')

def add_like(request, tweet_id):

    tweet = Tweet.objects.get(id= tweet_id)
    user = request.user
   # user.tweet_set.add(tweet)
    time = tweet.date_time
    tweet.likes += 1
    tweet.date_time = time
    tweet.save()
    return redirect('feed')

def retweet(request, tweet_id):
    tweet = Tweet.objects.get(id= tweet_id)
    user = request.user
   # user.tweet_set.add(tweet)
    time = tweet.date_time
    tweet.retweets += 1
    tweet.date_time = time
    user.tweet_set.add(tweet)
    tweet.save()
    return redirect('feed')