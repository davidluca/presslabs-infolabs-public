import pytest
from domainCheck.models import Report, Feature


@pytest.mark.django_db
def test_report():
    created_report = Report(domain='www.google.com', state='pending')
    assert created_report.domain == 'www.google.com'

@pytest.mark.django_db
def test_bad_domain_report():
    try:
        created_report = Report(domain='google.com', state='pending')
        assert False
    except:
        assert True

@pytest.mark.django_db
def test_no_domain_report():
    try:
        created_report = Report(state='pending')
        assert False
    except:
        assert True

@pytest.mark.django_db
def test_get_report_exists():
    created_report = Report.objects.get(domain='www.google.com')
    assert created_report.domain == 'www.example.com'


@pytest.mark.django_db
def test_get_report_not_exists():
    try:
        created_report = Report.objects.get(domain='not_extist')
        assert False
    except:
        assert True

@pytest.mark.django_db
def test_get_feature_exists():
    created_report = Feature.objects.get(question='www.google.com')
    assert created_report.domain == 'www.example.com'
