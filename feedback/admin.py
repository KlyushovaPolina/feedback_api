from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_type', 'description', 'created_at', 'file')

    list_filter = ('feedback_type', 'created_at')

    search_fields = ('description',)

    ordering = ('-created_at',)

    # Поля, доступные для редактирования
    fields = ('feedback_type', 'description', 'file')