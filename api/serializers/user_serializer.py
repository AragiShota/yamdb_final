import logging
from logging.handlers import RotatingFileHandler

from django.contrib.auth import authenticate
from rest_framework import exceptions, serializers, validators
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from ..models.user import User
from ..models.user_confirm_code_db import UserConfirmCodeDb


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,
                                     validators=[validators.UniqueValidator(
                                         queryset=User.objects.all()
                                     )])

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'bio',
                  'email',
                  'role',
                  ]


class RequestForRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = UserConfirmCodeDb
        fields = ['email']


class ConfirmRegistrationSerializer(TokenObtainSerializer):
    username_field = 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.EmailField()
        del self.fields['password']
        self.fields['confirm_code'] = serializers.CharField()

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'confirm_code': attrs['confirm_code'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            logger.error(KeyError, exc_info=True)
        if authenticate(**authenticate_kwargs):
            self.user = User.objects.update_or_create(
                email=attrs['email'],
                username=attrs['email']
            )[0]
            return {}
        raise exceptions.AuthenticationFailed(
            'No such request email-confirm code.')


class RegistrationSerializer(ConfirmRegistrationSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        UserConfirmCodeDb.objects.filter(email=attrs['email']).delete()
        return data


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s.')
logger = logging.getLogger(__name__)
handler = RotatingFileHandler(__file__ + '.log',
                              maxBytes=50000000,
                              backupCount=5,
                              )
logger.addHandler(handler)
