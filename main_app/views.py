from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User
from .models import Tweet
from .forms import TweetForm
from .forms import ProfileForm
from .models import Profile
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
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
       new_tweet.user = request.user
       new_tweet.date_time = date.today()
       #print(new_tweet)
       new_tweet.save()


       return redirect('feed')

def userFeed(request):
    profile = Profile.objects.get(user = request.user)
    print(profile)
    userTweetsList = Tweet.objects.filter(user = request.user)
    print(userTweetsList)
    form = TweetForm()
    return render(request, 'tweets/userTweets.html',  { 'userTweetsList': userTweetsList, 'form': form, 'profile': profile})

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

def user_detail(request, user_id):

    user = User.objects.get(id = user_id)
    profile = Profile.objects.get(user = user)
    user_tweets = user.tweet_set.all()
#create list of toys cat doesnt have
    return render(request, 'tweets/userDetailTweets.html', {'user_tweets': user_tweets, 'user': user, 'profile':profile})
