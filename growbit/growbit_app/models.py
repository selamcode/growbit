from django.db import models

# User model
class User(models.Model):
    user_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    title = models.CharField(max_length=30)
    
STATUS_CHOICES = [
    ('not_started', 'Not Started'),
    ('in_progress', 'In Progress'),
    ('completed',   'Completed'),
]
class Milestone(models.Model):
    # can be UUID for later if possible
    milestone_id  =  models.PositiveIntegerField()
    # 250 for now
    description =  models.TextField(max_length=250)
    achievable_tasks = models.TextField(max_length=150)
    assigned_to = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='not_started',
    )
class ProcessLog(models.Model):
    pass