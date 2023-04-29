from django.contrib import admin

# Register your models here.
from .models import Tweet
from .models import Profile

admin.site.register(Tweet)
admin.site.register(Profile)
