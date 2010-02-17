from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField
from PIL import Image
from Azul.process.models import Process
from hashlib import sha224

# Create your models here.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Tag(models.Model):
  name = models.CharField(max_length = 20)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Picture(models.Model):

  filename = models.CharField(max_length = 250)
  fingerprint = models.CharField(max_length = 60)
  tags = models.ManyToManyField(Tag)


#  def __init__(self, filename):
#    self.image = filename
#    self.fingerprint()

  def calculateFingerprint(self):
    img = Image.open(self.filename)
    return sha224(img.tostring()).hexdigest()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Process(Process):
  extra = models.CharField(max_length = 30)
