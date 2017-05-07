import pytest
from tests.fixtures import api_client
from django_dynamic_fixture import G
from domainCheck.models import Report, Feature


@pytest.mark.django_db
def test_create_report(api_client):
    response = api_client.post('/report/', {'domain':'https://www.facebook.com/'}, format='json')
    assert response.status_code == 201
    assert response.data['domain'] == 'https://www.facebook.com/'
    assert response.data['state'] == 'pending'


@pytest.mark.xfail
@pytest.mark.django_db
def test_bad_domain_field(api_client):
    response = api_client.post('/report/', {'domain':'sadsfas'}, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_without_domain_field(api_client):
    response = api_client.post('/report/', {'domain':''}, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_report(api_client):
    report1 = G(Report)  # create report
    response = api_client.get('/report/{}/'.format(report1.id))  # dynamic id
    assert response.status_code == 200
    assert response.data['domain'] == report1.domain 
    

@pytest.mark.django_db
def test_get_nonexisting_report(api_client):
    response = api_client.get('/report/-1/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_feature(api_client):
    feature = G(Feature) # create feature
    response = api_client.get('/feature/{}/'.format(feature.id))  # dynamic id
    assert response.status_code == 200
    assert response.data['name'] == '1'
    

@pytest.mark.xfail
@pytest.mark.django_db
def test_create_feature(api_client):
    response = api_client.post('/feature/', {'name':'featureName'}, format='json')
    assert response.status_code == 405
    assert response.data['name'] == 'featureName'
