from rest_framework import serializers

from service.models import Documents


class DocumentObjectSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    
    class Meta:
        model = Documents
        fields = [
            'id',
            'unique_name',
            'upload_name',
            'description',
            'link',
            'type',
            'format',
            'user_id',
            'created_at',
            'updated_at'
        ]

    def get_type(self, obj):
        return {
            "id": obj.type.id,
            "name": obj.type.name
        } if obj.type else None
