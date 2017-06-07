import pytest
from tests.fixtures import api_client
from django_dynamic_fixture import G
from domainCheck.models import Report, Feature


@pytest.mark.django_db
def test_create_report(api_client):
    response = api_client.post(
        '/report/', {'domain': 'https://www.facebook.com/'}, format='json'
    )
    assert response.status_code == 201, response.data
    assert response.data['domain'] == 'www.facebook.com'
    assert response.data['state'] == 'pending'


@pytest.mark.django_db
def test_bad_domain_field(api_client):
    response = api_client.post(
        '/report/', {'domain': 'sasdfsa'}, format='json'
    )
    assert response.data == { 'domain': ['Not a valid domain.'] } 
    assert response.status_code == 400


@pytest.mark.django_db
def test_without_domain_field(api_client):
    response = api_client.post('/report/', {'domain': ''}, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_report(api_client):
    report1 = G(Report)
    response = api_client.get('/report/{}/'.format(report1.id))
    assert response.status_code == 200
    assert response.data['domain'] == report1.domain
    assert response.data['state'] == report1.state
    assert (response.data['created_at'] ==
            report1.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))


@pytest.mark.django_db
def test_get_nonexisting_report(api_client):
    response = api_client.get('/report/-1/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_feature(api_client):
    feature = G(Feature)
    response = api_client.get('/feature/{}/'.format(feature.id))
    assert response.status_code == 200
    assert response.data['name'] == '1'


@pytest.mark.xfail
@pytest.mark.django_db
def test_create_feature(api_client):
    response = api_client.post(
        '/feature/', {'name': 'featureName'}, format='json'
    )
    assert response.status_code == 405

