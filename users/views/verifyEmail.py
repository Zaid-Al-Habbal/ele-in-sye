from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

from users.tokens import EmailVerificationToken 

User = get_user_model()

class VerifyEmailView(APIView):
    def get(self, request):
        token = request.GET.get('token')

        try:
            # access_token = AccessToken(token)
            # user_id = access_token['user_id']
            email_token = EmailVerificationToken(token)
            user_id = email_token['user_id']
            user = User.objects.get(id=user_id)

            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

class ResendVerificationEmailView(APIView):
        
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            if user.is_verified:
                return Response({'message': 'Email already verified'}, status=200)

            # token = get_tokens_for_user(user)['access']
            token = str(EmailVerificationToken.for_user(user))
            verify_url = f"http://localhost:8000/api/users/verify-email/?token={token}"

            send_mail(
                subject="Verify your email",
                message=f"Click the link to verify: {verify_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
            return Response({'message': 'Verification email sent'}, status=200)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
