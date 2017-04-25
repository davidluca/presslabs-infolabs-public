from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django_dynamic_fixture import G, new
from domainCheck.models import Report, Feature


class Command(BaseCommand):
	help = 'Help.'
	def handle(self, *args, **options):
		report1 = G(Report)
		report2 = G(Report)
		# Generate Features
		feature1 = G(Feature, Report = report1)
		feature2 = G(Feature, Report = report1)
		feature3 = G(Feature, Report = report2)
		feature4 = G(Feature, Report = report2)
		# Generate Admin
		admin = User.objects.get_or_create(username = 'admin')
		admin.is_staff =True
		admin.set_password("admin")
		admin.save()