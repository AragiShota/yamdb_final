from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title import Title
from .user import User


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Здесь пишем текст отзыва',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True,
        help_text='Указывается автоматически'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Укажите автора отзыва',
    )
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Укажите произведение'
    )
    score = models.IntegerField(
        verbose_name='Рейтинг',
        default=0,
        validators=[
            MinValueValidator(1, 'Оценка не может быть менее 1.'),
            MaxValueValidator(10, 'Оценка не может быть более 10.')
        ],
        help_text='Оценка по вашему мнению'
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]
