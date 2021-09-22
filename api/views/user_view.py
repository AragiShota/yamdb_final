from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models.user import User
from api.models.user_confirm_code_db import UserConfirmCodeDb
from api.permissions import AdminRequired, ForUsers
from api.serializers.user_serializer import (RegistrationSerializer,
                                             RequestForRegistrationSerializer,
                                             UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """Работа с зарегистрированными пользователями."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (AdminRequired, )
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['username', ]

    @action(methods=['get', 'patch'],
            permission_classes=[ForUsers, ],
            detail=False)
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer_class()
            data = serializer(request.user).data
            return Response(data, status=status.HTTP_200_OK)
        serializer = self.get_serializer_class()(request.user,
                                                 data=request.data,
                                                 partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestForRegistrationView(CreateAPIView):
    """Запрос на регистрацию."""
    queryset = UserConfirmCodeDb.objects.all()
    serializer_class = RequestForRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RequestForRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_email = serializer.validated_data['email']
        confirm_code = Token.generate_key(self.request)
        UserConfirmCodeDb.objects.update_or_create(
            email=user_email,
            confirm_code=confirm_code,
        )
        send_mail(
            'Registration on Yamdb',
            f'Your access token: {confirm_code}.',
            None,
            [user_email]
        )
        return Response(f'Email was sent to {user_email}',
                        status=status.HTTP_200_OK)


class RegistrationView(TokenObtainPairView, CreateModelMixin):
    """Регистрация пользователя."""
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny, )
