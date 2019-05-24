from django.db import models


class Dashboard(models.Model):
    engagement_name = models.CharField(max_length=200)
    hosts = models.IntegerField

class Host(models.Model):
    ip_address = models.CharField
    label = models.CharField
    type = models.CharField
    operating_systemn = models.CharField
    notes = models.CharField

class HostServices(models.Model):
    port = models.IntegerField
    protocol = models.CharField
    service = models.CharField
    version = models.CharField
    status = models.CharField

class Credentials(models.Model):
    service = models.CharField
    username = models.CharField
    password = models.CharField
    hash = models.CharField
