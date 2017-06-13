from rest_framework import serializers
from django.core.exceptions import ValidationError
from domainCheck.models import Report, Feature

from urllib.parse import urlparse
from django.core.validators import RegexValidator


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('url', 'domain', 'state', 'created_at')

    def validate_domain(self, value):
        parsed_url = urlparse(value)
        print (parsed_url)
        if not parsed_url.hostname:
            raise ValidationError(('Not a valid domain.'))
        domain_validator = RegexValidator(
            regex=(r'^(?=[a-z0-9\-\.]{3,253}$)([a-z0-9](()'
                   '([a-z0-9\-]){,61}[a-z0-9])?\.)+([a-z]{2,63})$'),
            message='Not a valid domain.',
        )
        domain_validator(parsed_url.hostname)
        return parsed_url.hostname


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = ('url', 'name', 'value', 'compare_value', 'report')
