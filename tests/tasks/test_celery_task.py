import pytest
from domainCheck.tasks import perform_check
from datetime import timedelta, datetime
from django_dynamic_fixture import G
from domainCheck.models import Report, Feature
from requests import RequestException


@pytest.mark.django_db
def test_perform_check_success(settings):
    report1 = G(Report, domain="https://presslabs.com")
    settings.CELERY_ALWAYS_EAGER = True
    settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
    res = perform_check.apply_async(args=[report1.id, ], propagate=True)
    features = report1.features.all()
    assert res.state == 'SUCCESS'
    assert features[0].name == 'ResponseTimeFeature'


@pytest.mark.django_db
def test_perform_check_failure_non_existent_id(settings):
    with pytest.raises(Report.DoesNotExist):
        report1 = G(Report, domain="https://presslabs.com")
        settings.CELERY_ALWAYS_EAGER = True
        settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
        res = perform_check.apply_async(args=[report1.id+1, ], propagate=True)


@pytest.mark.django_db
def test_perform_check_failure_invalid_domain(settings):
    with pytest.raises(RequestException):
        report1 = G(Report, domain="asdasfa")
        settings.CELERY_ALWAYS_EAGER = True
        settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
        res = perform_check.apply_async(args=[report1.id, ], propagate=True)
