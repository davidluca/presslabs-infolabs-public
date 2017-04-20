from rest_framework import routers
from infolabs.domainCheck import views

router = routers.DefaultRouter()
router.register(r'domaincheck', views.DomainCheckViewSet)
router.register(r'feature', views.FeatureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
