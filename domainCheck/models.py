from __future__ import unicode_literals
import datetime
from jsonfield import JSONField
from django.db import models
from django.utils import timezone


class Report(models.Model):
	domain = models.CharField(max_length=200)
	FINISHED = 'finished'
	PENDING = 'pending'
	REPORT_STATES = (
		(PENDING, 'pending'),
		(FINISHED, 'finished'))
	state = models.CharField(
		max_length=200, 
		choices=REPORT_STATES, 
		default=PENDING)
	created_at = models.DateTimeField(default=timezone.now)


class Feature(models.Model):
	name = models.CharField(max_length=200)
	value = JSONField()
	compare_value = JSONField()
	report = models.ForeignKey(
		'Report', on_delete=models.CASCADE)

	class Meta:
		unique_together = (('report','name'),)

	def state(self):
		return self.state in (self.FINISHED, self.PENDING)
