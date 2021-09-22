from django.db import models


class UserConfirmCodeDb(models.Model):
    email = models.EmailField('Адрес электронной почты',
                              unique=True)
    confirm_code = models.CharField('Токен регистрации',
                                    max_length=40)
