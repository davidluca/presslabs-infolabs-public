from django.core.management.base import BaseCommand, CommandError
from domainCheck.models import Report, Feature
from django_dynamic_fixture import G, get
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        report1 = G(Report)
        report2 = G(Report)
        feature1 = G(Feature, Report=report1)
        feature2 = G(Feature, report=report1)
        feature3 = G(Feature, report=report2)
        feature4 = G(Feature, report=report2)
        user1, _ = User.objects.get_or_create(username="admin")
        user1.is_staff = True
        user1.set_password("admin")
        user1.save()
