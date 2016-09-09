from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HomepageVisits(models.Model):
	count = models.IntegerField(default=0)