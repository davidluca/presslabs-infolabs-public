from rest_framework import serializers
from django.core.exceptions import ValidationError
from domainCheck.models import Report, Feature
from urllib.parse import urlparse


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('url', 'domain', 'state', 'created_at')
    
    def validate_domain(self, value):
        parsed_url = urlparse(value)
        print (parsed_url)
        if not parsed_url.hostname:
            raise ValidationError(('URL is not valid.'))
        return parsed_url.hostname


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = ('url', 'name', 'value', 'compare_value', 'report')