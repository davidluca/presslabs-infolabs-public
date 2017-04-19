from domainCheck.models import DomainCheck, Feature
from rest_framework import viewsets
from infolabs.domainCheck.serializers import DomainCheckSerializer, FeatureSerializer


class DomainCheckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DomainCheck.objects.all().order_by('-date_joined')
    serializer_class = DomainCheckSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
