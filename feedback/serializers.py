from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'feedback_type', 'description', 'file', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_file(self, value):
        if value:
            # Ограничение размера файла (5 МБ)
            max_size = 5 * 1024 * 1024
            if value.size > max_size:
                raise serializers.ValidationError("Файл слишком большой. Максимальный размер: 5 МБ.")
        return value

    def validate_description(self, value):
        # Проверка, что описание не пустое
        if not value.strip():
            raise serializers.ValidationError("Описание не может быть пустым.")
        return value