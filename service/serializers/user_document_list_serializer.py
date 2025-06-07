from rest_framework import serializers

from service.serializers import DocumentObjectSerializer


class UserDocumentListSerializer(serializers.Serializer):
    documents = DocumentObjectSerializer(many=True)
