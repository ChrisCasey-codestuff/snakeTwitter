from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User
from .models import Tweet
from .forms import TweetForm
from datetime import date
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


       return redirect('feed/')

def userFeed(request):
    userTweetsList = Tweet.objects.filter(user = request.user)

    form = TweetForm()
    return render(request, 'tweets/userTweets.html',  { 'userTweetsList': userTweetsList, 'form': form})



