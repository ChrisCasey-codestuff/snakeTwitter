from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User



class Tweet (models.Model):

    content = models.TextField( max_length=250, verbose_name='')
    date_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (f'{self.content}')
    class Meta:
        ordering = ['-date_time']
    def get_absolute_url(self):

        return reverse('feed')

class Profile (models.Model):

    bio = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (f'{self.bio}')

    def get_absolute_url(self):

        return reverse('feed')


