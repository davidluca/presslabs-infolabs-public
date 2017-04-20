from domainCheck.models import Report, Feature
from rest_framework import viewsets
from domainCheck.serializers import ReportSerializer, FeatureSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
