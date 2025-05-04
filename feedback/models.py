from django.db import models

FEEDBACK_TYPES = (
    ('wishlist', 'Пожелание'),
    ('problem', 'Проблема'),
    ('claim', 'Претензия'),
    ('other', 'Другое'),
)

class Feedback(models.Model):
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPES, verbose_name='Тип обращения')
    description = models.TextField(verbose_name='Описание')
    file = models.FileField(upload_to='feedback_files/', null=True, blank=True, verbose_name='Файл')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.get_feedback_type_display()} - {self.created_at}" #тип - время создания, для админки

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'