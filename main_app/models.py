from django.db import models

# Create your models here.
class User (models.Model):
    username = models.CharField( max_length=50 )
    password = models.TextField( max_length=250 )
    def __str__(self):
        return ({self.name})

class Tweet (models.Model):
    content = models.TextField( max_length=250 )
    date_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return ({self.name})
