from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория',
        max_length=200,
        help_text='Укажите категорию',
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=130,
        unique=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
