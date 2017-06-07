from __future__ import absolute_import, unicode_literals

import importlib
import logging

from celery import shared_task
from django.conf import settings
from domainCheck.models import Report

logger = logging.getLogger(__name__)


@shared_task
def perform_check(report_id):
    report = Report.objects.get(pk=report_id)
    domain = report.domain
    for crawler_name, module_path in settings.CRAWLERS:
        module = importlib.import_module(module_path)
        crawler = getattr(module, crawler_name)
        crawler_instance = crawler()
        crawler_instance.crawl(domain)

