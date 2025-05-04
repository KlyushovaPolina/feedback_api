from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'feedback_type', 'description', 'file', 'created_at']
        read_only_fields = ['id', 'created_at']