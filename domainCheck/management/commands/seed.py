from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django_dynamic_fixture import G
from domainCheck.models import Report, Feature


class Command(BaseCommand):
    help = 'Initial generated data.'
    def handle(self, *args, **options):
        report1 = G(Report)
        report2 = G(Report)
        # Generate Features
        feature1 = G(Feature, report = report1)
        feature2 = G(Feature, report = report1)
        feature3 = G(Feature, report = report2)
        feature4 = G(Feature, report = report2)
        # Generate Admin
        admin, _ = User.objects.get_or_create(username = 'admin')
        admin.is_staff =True
        admin.is_superuser = True
        admin.is_admin = True
        admin.set_password("admin")
        admin.save()