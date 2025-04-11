from rest_framework import serializers
from categories.models import Category

# We will use this serializer when the user request ALL or a LIST of categories:
# --------------------------------------------------------------------------------
class CategoryListSerializer(serializers.ModelSerializer):
    parent_name = serializers.StringRelatedField(source='parent', read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at',
            'parent',
            'parent_name'
        ]

        read_only_fields = ["created_at", "updated_at"]    

#for return subcategories with the category requested: we used RecursiveField class
# --------------------------------------------------------------------------------
class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CategoryDetailSerializer(serializers.ModelSerializer):
    subcategories = RecursiveField(many=True, read_only=True)
    parent_name = serializers.StringRelatedField(source='parent', read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at',
            'parent',
            'parent_name',
            'subcategories'
        ]

        read_only_fields = ["created_at", "updated_at"]    
    