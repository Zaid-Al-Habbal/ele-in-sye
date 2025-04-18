from rest_framework_simplejwt.tokens import Token
from datetime import timedelta

class EmailVerificationToken(Token):
    lifetime = timedelta(hours=24)  # valid for 24 hours
    token_type = "email"
    lifetime_claim = "exp"
