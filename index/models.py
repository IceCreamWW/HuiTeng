from django.db import models


class Notifications(models.Model):
    summary = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    expiration = models.DateTimeField('date outdated')

