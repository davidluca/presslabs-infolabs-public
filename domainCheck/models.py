from __future__ import unicode_literals
import datetime
from jsonfield import JSONField
from django.db import models
from django.utils import timezone


class Report(models.Model):
	domain = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	created_at = models.DateTimeField()


class Feature(models.Model):
	name = models.CharField(max_length=200)
	value = JSONField()
	compare_value = JSONField()
	report = models.ForeignKey('Report', on_delete=models.CASCADE)

	class Meta:
		unique_together = (('report', 'name'))
