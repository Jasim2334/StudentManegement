import pytest
from .factories import StudentFactory
from core.tests.conftests import api_client
pytestmark = pytest.mark.django_db


class TestBlogCRUD:
    def test_create_blog(self, api_client):
        data = {
            "name": "Md Jasim",
            "age": "22",
            "roll": "1002",
            "marks" : "345",
            "gender" : "M",
            "subject" : "Python"
            }

        response = api_client.post('/student/', data=data,format="json")
        assert response.status_code == 201
        returned_json = response.json()
        assert 'id' in returned_json
        assert returned_json['name'] == data['name']
        assert returned_json['age'] == data['age']
        assert returned_json['roll'] == data['roll']
        assert returned_json['marks'] == data['marks']
        assert returned_json['gender'] == data['gender']
        assert returned_json['subject'] == data['subject']

    def test_retrieve_blogs(self, api_client):
        StudentFactory.create_batch(5)
        response = api_client.get('/student/',format="json")
        assert response.status_code == 200
        assert len(response.json()) == 5

    def test_delete_blog(self, api_client):
        student = StudentFactory()
        url = f"/student/{student.id}/"
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_update_blog(self, api_client):
        student = StudentFactory()
        data = {
            "name": "Taha",
            "age": "43",
            "roll": "1005",
            "marks" : "312",
            "gender" : "F",
            "subject" : "Java"
            }
        url = f"/student/{student.id}/"

        response = api_client.patch(url, data=data,format="json")
        assert response.status_code == 200
        returned_json = response.json()
        assert returned_json['name'] == data['name']
        assert returned_json['age'] == data['age']
        assert returned_json['roll'] == data['roll']
        assert returned_json['marks'] == data['marks']
        assert returned_json['gender'] == data['gender']
        assert returned_json['subject'] == data['subject']