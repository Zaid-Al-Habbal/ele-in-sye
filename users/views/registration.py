from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers.registration import RegisterSerializer
from django.core.mail import send_mail
from django.conf import settings

from users.tokens import EmailVerificationToken

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def get_verification_token(self, user):
        return str(EmailVerificationToken.for_user(user))

    def perform_create(self, serializer):
        user = serializer.save()
        token = self.get_verification_token(user)
        verify_url = f"http://localhost:8000/api/users/verify-email/?token={token}"

        send_mail(
            subject="Welcome to Ele-In-Sye",
            message=f"After creating your account you need to verify it, so click the link to verify: {verify_url}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],  # now user.email is a real string
        )
