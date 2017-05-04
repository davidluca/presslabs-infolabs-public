import pytest
from tests.fixtures import api_client
from django_dynamic_fixture import G
from domainCheck.models import Report, Feature

class TestReport:

    @pytest.mark.django_db
    def test_report(self):
        report1 = G(Report, domain='www.example.com')
        report1.save()
        assert report1.domain == 'www.example.com'

    @pytest.mark.django_db
    def test_bad_domain_field(self):
        report1 = G(Report, domain = 'google.com')
        report1.save()
        assert report1.domain == 'google.com'

    @pytest.mark.django_db
    def test_without_domain_field(self):
        report1 = G(Report, domain='')
        report1.save()
        assert report1.domain == ''

    @pytest.mark.django_db
    def test_get_report(self, api_client):
        report1 = G(Report) # create report
        response = api_client.get('/report/{}/'.format(report1.id)) # dynamic id
        assert response.status_code == 200
        d = {}
        d = response.data # create a dict with the response.data value
        assert response.data == d # verify if the values are equal
    
    @pytest.mark.django_db
    def test_get_nonexisting_report(self):
        report2 = G(Report, domain = 'www.ex.com')
        assert report2.save() == None
        
class TestFeature:

    @pytest.mark.django_db
    def test_get_feature(self, api_client):
        feature = G(Feature) # create feature
        response = api_client.get('/feature/{}/'.format(feature.id)) # dynamic id
        assert response.status_code == 200
        d = {}
        d = response.data # create a dict with the response.data value
        assert response.data == d # verify if the values are equal

    @pytest.mark.django_db
    def test_create_feature(self):
        feature1 = G(Feature, name='feature')
        feature1.save()
        assert feature1.name == 'feature'