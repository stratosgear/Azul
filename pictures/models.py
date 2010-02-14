from django.db import models
from Azul.process.models import Process

# Create your models here.

class Pictures(models.Model):
  filename = models.FilePathField()


class PicProcess(Process):
  extra = models.CharField(max_length = 30)
