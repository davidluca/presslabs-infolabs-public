from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class DomainCheck(models.Model):
	domain = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	create_date = models.DateTimeField()
	feature = models.ForeignKey('Feature',
		on_delete=models.CASCADE)

class Feature(models.Model):
	name = models.CharField(max_length=200)
	value = models.CharField(max_length=200)
	compare_value = models.CharField(max_length=200)
