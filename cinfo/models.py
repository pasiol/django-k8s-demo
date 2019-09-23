from django.db import models

# Create your models here.
class Request(models.Model):
    id = models.AutoField(primary_key=True)
    container_id = models.UUIDField()
    user_agent = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)
