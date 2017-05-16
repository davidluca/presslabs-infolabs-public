from __future__ import unicode_literals
from jsonfield import JSONField
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from urllib.parse import urlparse

class Report(models.Model):
    FINISHED = 'finished'
    PENDING = 'pending'
    REPORT_STATES = (
        (PENDING, 'pending'),
        (FINISHED, 'finished'))
    domain = models.CharField(
        max_length=200,
        #validators=[RegexValidator(regex='^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\.[a-zA-Z]{2,3})$')]
        )
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

