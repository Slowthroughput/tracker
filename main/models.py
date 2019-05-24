import datetime
from django.db import models
from django.utils import timezone


class Dashboard(models.Model):
    engagement_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    hosts = models.IntegerField

    def __str__(self):
        return self.engagement_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Host(models.Model):
    host_name = models.CharField
    ip_address = models.CharField
    label = models.CharField
    type = models.CharField
    operating_system = models.CharField
    notes = models.CharField

    def __str__(self):
        return self.host_name

class HostServices(models.Model):
    port = models.IntegerField
    protocol = models.CharField
    service = models.CharField
    version = models.CharField
    status = models.CharField

    def __str__(self):
        return self.port

class Credentials(models.Model):
    service = models.CharField
    username = models.CharField
    password = models.CharField
    hash = models.CharField

    def __str__(self):
        return self.username

