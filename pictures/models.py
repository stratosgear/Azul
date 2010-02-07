from django.db import models

# Create your models here.

class pictures(models.Model):
  filename = models.FilePathField()
