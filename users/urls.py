from django.urls import path
# from rest_framework_simplejwt.views import TokenRefreshView

from .views.registration import RegisterView
from .views.verifyEmail import VerifyEmailView, ResendVerificationEmailView
from .views.login import LoginView
from .views.logout import LogoutView
from .views.refreshToken import CustomTokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification/', ResendVerificationEmailView.as_view(), name='resend-verification'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='custom_token_refresh'),
]
