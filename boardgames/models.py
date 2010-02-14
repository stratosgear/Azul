from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField


class Player(models.Model):
  name = models.CharField(max_length = 30)
  initials = models.CharField(max_length = 5)
  avatar = ImageWithThumbnailsField(
    upload_to = 'avatars',
    thumbnail = {'size': (100, 100)},
    extra_thumbnails = {
        'sm': {'size': (16, 16), 'options': ['crop', 'upscale']},
        'medium': {'size': (32, 32)},
    },
  )

  def __unicode__(self):
    return self.name


