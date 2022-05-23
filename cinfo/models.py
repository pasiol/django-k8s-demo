from django.db import models


class Worker(models.Model):
    worker_id = models.UUIDField(primary_key=True)
    hostname = models.CharField(max_length=128)
    fqdn = models.CharField(max_length=256)
    ip_address = models.CharField(max_length=32)
    mac_address = models.CharField(max_length=17)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('worker_id', 'mac_address')


# Create your models here.
class Request(models.Model):
    id = models.AutoField(primary_key=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)

