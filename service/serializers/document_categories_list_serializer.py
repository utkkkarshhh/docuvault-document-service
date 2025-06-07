from rest_framework import serializers

from service.models import DocumentCategoryMaster


class DocumentCategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategoryMaster
        fields = [
            'id',
            'name'
        ]
