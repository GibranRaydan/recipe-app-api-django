from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

from core.models import Task

TASK_URL = reverse('task:task-list')


class PublicTaskTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list_of_tasks(self):
        Task.objects.create(
            title='sommetitle', description='somedescription'
        )
        res = self.client.get(TASK_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_task_success(self):
        payload = {
            'title': 'new example',
            'description': 'this is a new description'
        }
        res = self.client.post(TASK_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
