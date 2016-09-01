from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

import datetime

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
	category_name = models.CharField(max_length=50)

	def __str__(self):
		return self.category_name



@python_2_unicode_compatible
class Society(models.Model):
	society_name = models.CharField(max_length=80)
	society_description = models.TextField()
	society_user = models.OneToOneField(User)
	society_category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.society_name




@python_2_unicode_compatible
class Notice(models.Model):
	event_name = models.CharField(max_length=100)
	event_description = models.TextField()
	event_date = models.DateField(null=True, blank=True)
	event_time = models.TimeField(null=True, blank=True)
	event_link = models.URLField(max_length=200)
	event_date_launched = models.DateField(auto_now=True)
	event_duration = models.IntegerField()
	event_society = models.ForeignKey(Society, on_delete=models.CASCADE)

	def __str__(self):
		return self.event_name

