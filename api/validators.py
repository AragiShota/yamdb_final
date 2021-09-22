from datetime import datetime

from rest_framework.exceptions import ValidationError


def year_validator(value):
    if value > datetime.now().year:
        raise ValidationError(
            'Значение года выпуска не может быть больше значения текущего года'
        )
