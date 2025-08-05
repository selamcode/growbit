from django.contrib import admin
from growbit_app.models import User, Milestone,Task, Level, ProgressLog 

models = (User, Milestone,Task, Level, ProgressLog)
admin.site.register(models)
# Register your models here.
