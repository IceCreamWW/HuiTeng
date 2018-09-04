from django.db import models
from separatedvaluesfield.models import SeparatedValuesField


class Notifications(models.Model):
    summary = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    expiration = models.DateTimeField('date outdated')

    class Meta:
        ordering = ['-pub_date', '-expiration']


class Certificates(models.Model):
    name = models.CharField(max_length=20)
    cover_img_path = models.CharField(max_length=256)
    all_img_paths = SeparatedValuesField(max_length=512, token=',')
    visible = models.BooleanField()

    @property
    def html_name(self):
        return self.name.replace('-', '\n')

    @property
    def description_name(self):
        return self.name.replace('-', ':')
