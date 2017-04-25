from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def perform_check(check_id):
	return "Check id is %s" % check_id