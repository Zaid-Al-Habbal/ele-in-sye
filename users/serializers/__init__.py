from .registration import RegisterSerializer
from .login import LoginSerializer

# It’s a list that defines which names will be exported when the module is imported using from ... import *
__all__ = ["RegisterSerializer", "LoginSerializer"]