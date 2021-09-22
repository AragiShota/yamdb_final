from rest_framework import authentication

from .models.user_confirm_code_db import UserConfirmCodeDb


class ConfirmUserRegistrationAuthentication(authentication.BaseAuthentication):
    """Аутентификация будущего пользователя."""
    def authenticate(self, request, email=None, confirm_code=None):
        try:
            return UserConfirmCodeDb.objects.get(
                email=email, confirm_code=confirm_code)
        except UserConfirmCodeDb.DoesNotExist:
            return None
