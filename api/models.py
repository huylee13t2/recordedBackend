from django.db import models

# Create your models here.
class Recorder(models.Model):
    videoId = models.CharField(max_length=200)