from http import HTTPStatus

from django.test import Client, TestCase

from backend.api import models


class TaskiTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_list_available(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_uncompleted_task(self):
        data = {
            "title": "Title",
            "description": "Descr"
        }
        response = self.client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(
            models.Task.objects.get(
                title=data["title"],
                description=data["description"]
            ).exists()
        )