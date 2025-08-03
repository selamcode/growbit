from django.db import models
from django.utils import timezone

class User(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('ic', 'Individual Contributor'),
    ]
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)  # Removed default
    user_level = models.ForeignKey("Level", on_delete=models.SET_NULL, null=True, related_name='users')

    def __str__(self):
        return self.username


class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=50)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="custom_levels")

    def __str__(self):
        return self.level_name


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    task_level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.task_name


class Milestone(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    ms_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    start_date = models.DateField()
    due_date = models.DateField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_milestones')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_milestones')
    milestone_level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='milestones')
    tasks = models.ManyToManyField(Task, related_name='milestones')

    created_at = models.DateTimeField(auto_now_add=True)  # Removed default

    def __str__(self):
        return self.title


class ProgressLog(models.Model):
    pl_id = models.AutoField(primary_key=True)
    log_ms = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='progress_logs')
    log_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_logs')
    progress_log = models.TextField()
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Removed default

    def __str__(self):
        return f"Log by {self.log_owner.username} on {self.log_ms.title}"
