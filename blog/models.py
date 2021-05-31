from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class user(models.Model):
    user = models.CharField(max_length=32, verbose_name=_('user'))