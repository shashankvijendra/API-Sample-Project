from django.db import models

# Create your models here.

class Lkstatuscode(models.Model):
    lk_status_code = models.CharField(primary_key=True, max_length=255)
    lk_status_name = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)
    
    
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    task_for = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now=True, null=True)
    lk_status_code = models.ForeignKey(Lkstatuscode, on_delete=models.CASCADE)
