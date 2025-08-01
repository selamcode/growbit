from django.db import models

# User model
class User(models.Model):
    user_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    title = models.CharField(max_length=30)
class Milestone(models.Model):
    pass
