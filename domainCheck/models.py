from __future__ import unicode_literals
from urllib.parse import urlparse

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from jsonfield import JSONField

class Report(models.Model):
    FINISHED = 'finished'
    PENDING = 'pending'
    REPORT_STATES = (
        (PENDING, 'pending'),
        (FINISHED, 'finished'))
    domain = models.CharField(max_length=200,)
    state = models.CharField(
        max_length=8,
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
        unique_together = (('report', 'name'),)

