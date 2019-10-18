from django.db import models
from uuid import uuid4
from datetime import date
import os
# Create your models here.

# add this
class Employees(models.Model):
  first_name = models.CharField(max_length=120)
  last_name = models.CharField(max_length=120)
  about = models.TextField()

  def _upload_avatar(instance, filename):
      extension = os.path.splitext(filename)[1][1:]
      directory = instance.__class__.__name__
      url = os.path.join('avatar', directory, date.today().strftime("%Y/%m"))
      file_name = '{}.{}'.format(uuid4().hex, extension)

      return os.path.join(url, file_name)

  def _upload_files(instance, filename):
      extension = os.path.splitext(filename)[1][1:]
      directory = instance.__class__.__name__
      url = os.path.join('cv', directory, date.today().strftime("%Y/%m"))
      file_name = '{}.{}'.format(uuid4().hex, extension)

      return os.path.join(url, file_name)

  avatar = models.ImageField(upload_to=_upload_avatar)
  cv = models.FileField(upload_to=_upload_files)

  def _str_(self):
    return self.first_name