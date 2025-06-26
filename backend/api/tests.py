from http import HTTPStatus
from backend.api import models
from django.test import Client, TestCase


class TaskiTestCase(TestCase):
    def setup(self):
        self.client = Client()

    def test_api_list_available(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_uncompleted_tast(self):
        data = {
            "title": "Title",
            "description": "Descr"
        }
        response = self.client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.get(title=data["title"], description=data["description"]).exists())
