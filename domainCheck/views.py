from domainCheck.models import Report, Feature
from rest_framework import viewsets
from infolabs.domainCheck.serializers import ReportSerializer, FeatureSerializer


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer

    def get_queryset(self):
        user = self.request.user
        return Report.objects.filter(report=user)

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
