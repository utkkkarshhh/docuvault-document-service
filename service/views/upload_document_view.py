import uuid

from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.exceptions import BadRequestException
from service.models import Documents
from service.serializers import (DocumentObjectSerializer,
                                 UploadDocumentSerializer)
from service.utils import CommonUtils, ResponseHandler, Firebase


class UploadDocumentView(APIView):
    request_serializer_class = UploadDocumentSerializer
    response_serializer_class = DocumentObjectSerializer
    parser_classes = (MultiPartParser, FormParser)
    firebase_instance = Firebase()
    
    def post(self, request, *args, **kwargs):
        serializer = self.request_serializer_class(data=request.data)
        if not serializer.is_valid():
            error_message = CommonUtils.handle_serializer_error(serializer.errors)
            raise BadRequestException(error_message)
        validated_data = serializer.validated_data
        unique_file_name = self._generate_uuid_filename()
        document_link = self.firebase_instance.upload_file(file=validated_data.get('file'), filename=unique_file_name)
        document = self._create_document(validated_data, unique_file_name, document_link)
        document_object = self.response_serializer_class(document)
        return ResponseHandler(
            status=status.HTTP_201_CREATED,
            success=True,
            message=ResponseMessages.FILE_UPLOADED_SUCCESSFULLY,
            data=document_object.data
        )
        
    def _create_document(self, data, unique_file_name, document_link):
        document = Documents.objects.create(
            unique_name = unique_file_name,
            upload_name = data.get('name'),
            description = data.get('description'),
            type = data.get('type'),
            link = document_link,
            format = data.get('format'),
            user_id = data.get('user_id')
        )
        return document
        
    def _generate_uuid_filename(self):
        return uuid.uuid4()
