from django.db import models

from ..validators import year_validator
from .category import Category
from .genre import Genre


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Укажите название произведения',
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='жанры',
        related_name='titles'
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска',
        default=2021,
        blank=True,
        null=True,
        validators=[year_validator],
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
