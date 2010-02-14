from django.db import models

# Create your models here.
class Process(models.Model):
  pid = models.IntegerField()
  name = models.CharField(max_length = 40)
  parameters = models.TextField()
  progress = models.FloatField()



  def __unicode__(self):
    return "%s %s" % (self.pid, self.name)
