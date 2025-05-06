from django.test import TestCase
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Feedback

class FeedbackTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'feedback_type': 'problem',
            'description': 'Тестовое описание',
            'file': SimpleUploadedFile('test.txt', b'Test file content', content_type='text/plain'),
        }
        self.invalid_payload = {
            'feedback_type': 'invalid_type',
            'description': '',
        }

    def test_create_feedback_api(self):
        response = self.client.post('/feedback/api/', self.valid_payload, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Feedback.objects.count(), 1)
        self.assertEqual(Feedback.objects.first().feedback_type, 'problem')

    def test_invalid_feedback_api(self):
        response = self.client.post('/feedback/api/', self.invalid_payload, format='multipart')
        self.assertEqual(response.status_code, 400)

    def test_feedback_form_submission(self):
        response = self.client.post('/feedback/', self.valid_payload, format='multipart')
        self.assertEqual(response.status_code, 302)  # Перенаправление после успеха
        self.assertEqual(Feedback.objects.count(), 1)

    def test_model_str(self):
        feedback = Feedback.objects.create(feedback_type='wishlist', description='Test')
        self.assertIn('Пожелание', str(feedback))