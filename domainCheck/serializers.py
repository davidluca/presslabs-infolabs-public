from rest_framework import serializers
from status.models import DomainCheck, Feature

class DomainCheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Check
        fields = ('url', 'domain', 'state', 'create_date', 'feature')


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = ('url', 'name', 'value', 'compare_value')