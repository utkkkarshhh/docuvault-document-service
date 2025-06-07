from rest_framework import status
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.exceptions import BadRequestException
from service.serializers import DownloadDocumentSerializer
from service.utils import CommonUtils, ResponseHandler, Firebase
from service.models import Documents


class DownloadDocumentView(APIView):
    serializer_class = DownloadDocumentSerializer
    firebase = Firebase()
    
    def get_queryset(self, document_id, user_id):
        document = Documents.objects.filter(id=document_id, user_id=user_id).first()
        if document:
            return document
        if Documents.objects.filter(id=document_id).exists():
            raise BadRequestException(ResponseMessages.DOCUMENT_DOES_NOT_BELONG_TO_USER)
        raise BadRequestException(ResponseMessages.NO_DOCUMENT_FOUND_FOR_ID.format(document_id, user_id))
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            error_message = CommonUtils.handle_serializer_error(serializer.errors)
            raise BadRequestException(error_message)
        validated_data = serializer.validated_data
        document = self.get_queryset(validated_data.get('document_id'), validated_data.get('user_id'))
        filename = f"{document.unique_name}.{document.format}"
        file = self.firebase.generate_signed_url(filename)
        return ResponseHandler(
            status=status.HTTP_202_ACCEPTED,
            success=True,
            message=ResponseMessages.FILE_FETCHED_SUCCESSFULLY,
            data={
                'url': file
            }
        )
