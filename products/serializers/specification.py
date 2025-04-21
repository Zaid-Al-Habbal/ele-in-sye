from rest_framework import serializers
from products.models import ProductSpecification


class ProductSpecificationSerializer(serializers.ModelSerializer):
    template_name = serializers.StringRelatedField(source='template.name')

    class Meta:
        model = ProductSpecification
        fields = [
            'template',
            'template_name',
            'value'
        ]
    