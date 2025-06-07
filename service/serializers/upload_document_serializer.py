import os

from rest_framework import serializers

from service.constants import ResponseMessages, SupportedFileTypes
from service.exceptions import BadRequestException
from service.models import DocumentCategoryMaster


class UploadDocumentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    file = serializers.FileField(required=True)
    type = serializers.PrimaryKeyRelatedField(queryset=DocumentCategoryMaster.objects.all(), required=True)
    user_id = serializers.IntegerField(required=True)
    format = serializers.SerializerMethodField()

    def validate_file(self, value):
        format = os.path.splitext(value.name)[1][1:].lower()
        if format not in SupportedFileTypes.get_all_supported_formats():
            raise BadRequestException(ResponseMessages.FORMAT_NOT_SUPPORTED)
        return value

    def get_format(self, obj):
        file_obj = self.validated_data.get('file', None)
        if file_obj:
            return os.path.splitext(file_obj.name)[1][1:].lower()
        return None

    def validate(self, attrs):
        file_obj = attrs.get('file')
        if file_obj:
            attrs['format'] = os.path.splitext(file_obj.name)[1][1:].lower()
        return attrs
