from .product import Product
from .specification import ProductSpecification

# It’s a list that defines which names will be exported when the module is imported using from ... import *
__all__ = ["Product", "ProductSpecification"]