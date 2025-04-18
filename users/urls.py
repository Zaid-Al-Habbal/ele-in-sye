from django.urls import path
from .views.registration import RegisterView
from .views.verifyEmail import VerifyEmailView, ResendVerificationEmailView
from .views.login import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification/', ResendVerificationEmailView.as_view(), name='resend-verification'),
    path('login/', LoginView.as_view(), name='login'),
]
