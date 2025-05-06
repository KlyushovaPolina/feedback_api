from django.urls import path
from .views import FeedbackCreateAPIView, feedback_form_view

app_name = 'feedback'

urlpatterns = [
    path('api/', FeedbackCreateAPIView.as_view(), name='feedback_api'),
    path('', feedback_form_view, name='feedback_form'),
]
