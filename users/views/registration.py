from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers.registration import RegisterSerializer
from django.core.mail import send_mail
from django.conf import settings

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def perform_create(self, serializer):
        user = serializer.save()
        token = self.get_tokens_for_user(user)['access']
        verify_url = f"http://localhost:8000/api/users/verify-email/?token={token}"

        send_mail(
            subject="Verify your email",
            message=f"Click the link to verify: {verify_url}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],  # now user.email is a real string
        )
