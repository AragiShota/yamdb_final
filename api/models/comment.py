from django.db import models

from .review import Review
from .user import User


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Здесь пишем текст',
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
        related_name='comments',
        help_text='Укажите автора',
    )
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='Укажите отзыв'
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]
