from rest_framework import serializers
from domainCheck.models import Report, Feature


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('url', 'domain', 'state', 'created_at')


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = ('url', 'name', 'value', 'compare_value', 'report')
