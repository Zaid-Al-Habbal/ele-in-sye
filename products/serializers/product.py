from rest_framework import serializers
from products.models import Product, ProductSpecification
from .specification import ProductSpecificationSerializer


class ProductDetailSerializer(serializers.ModelSerializer):
    seller_name = serializers.StringRelatedField(source="seller")
    category_name = serializers.StringRelatedField(source="category")
    specifications = ProductSpecificationSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "condition",
            "location",
            "seller",
            "seller_name",
            "category",
            "category_name",
            "created_at",
            "updated_at",
            "specifications",
        ]
        read_only_fields = ["created_at", "update_at", "seller"]


    # override create method for writeable nested serializers:
    def create(self, validated_data):
        specs_data = validated_data.pop('specifications')
        product = Product.objects.create(**validated_data)
        for spec in specs_data:
            ProductSpecification.objects.create(product=product, **spec)

        return product

    def update(self, instance, validated_data):
        specs_data = validated_data.pop('specifications')
        instance = super().update(instance, validated_data)

        instance.specifications.all().delete()

        for spec in specs_data:
            ProductSpecification.objects.create(product=instance, **spec)

        return instance
    
    # check if there are duplicates templates
    def validate(self, data):
        templates = [item['template'] for item in data.get('specifications', [])]
        if len(templates) != len(set(templates)):
            raise serializers.ValidationError("Duplicate specification templates are not allowed.")
        return data

# {
#     "id": 10,
#     "title": "IPhone 14",
#     "description": "great mobile",
#     "price": "1500.00",
#     "condition": "used",
#     "location": "Damascus",
#     "seller": 5,
#     "seller_name": "Mohammed DADA",
#     "category": 1,
#     "category_name": "Smartphones",
#     "created_at": "2025-04-19T13:57:57.251334Z",
#     "updated_at": "2025-04-19T13:57:57.251376Z",
#     "specifications": [
#         {"template": 1, "template_name": "RAM", "value": "8"},
#         {"template": 2, "template_name": "Screen", "value": "14 inche"},
#         {"template": 3, "template_name": "OS", "value": "IOS"},
#     ],
# }

class ProductListSerializer(serializers.ModelSerializer):
    seller_name = serializers.StringRelatedField(source="seller")
    category_name = serializers.StringRelatedField(source="category")

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "price",
            "condition",
            "location",
            "seller",
            "seller_name",
            "category",
            "category_name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "update_at"]