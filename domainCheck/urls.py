from django.conf.urls import url, include
from rest_framework import routers
from domainCheck import views

router = routers.DefaultRouter()
router.register(r'report', views.ReportViewSet)
router.register(r'feature', views.FeatureViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
