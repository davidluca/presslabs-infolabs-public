import pytest
from domainCheck.tasks import perform_check
from datetime import timedelta, datetime
from django_dynamic_fixture import G
from domainCheck.models import Report


@pytest.mark.django_db
def test_perform_check(settings):
    report1 = G(Report, domain="https://presslabs.com")
    settings.CELERY_ALWAYS_EAGER = True
    settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
    res = perform_check.apply_async(args=[report1.id, ], propagate=True)
    print(res.state)
