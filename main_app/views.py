from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User
from .models import Tweet
# Create your views here.
def home(request):
  return render(request, 'base.html')

def user_detail(request):
  return render(request, 'users/userDetail.html')

def feed(request):
  tweetsList = Tweet.objects.all()
  return render(request, 'tweets/tweetsIndex.html',  { 'tweetsList': tweetsList })

