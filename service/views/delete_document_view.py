from rest_framework import status
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.exceptions import BadRequestException
from service.models import Documents
from service.serializers import DeleteDocumentSerializer
from service.utils import CommonUtils, Firebase, ResponseHandler


class DeleteDocumentView(APIView):
    serializer_class = DeleteDocumentSerializer
    firebase = Firebase()
    
    def get_queryset(self, document_id, user_id):
        return Documents.objects.filter(id=document_id, user_id=user_id).first()
    
    def delete(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            errors = CommonUtils.handle_serializer_error(serializer.errors)
            raise BadRequestException(errors)
        validated_data = serializer.validated_data
        document_id = validated_data.get('document_id')
        user_id = validated_data.get('user_id')
        document = self.get_queryset(document_id, user_id)
        if not document:
            raise BadRequestException(ResponseMessages.NO_DOCUMENT_FOUND_FOR_ID.format(document_id, user_id))
        filename = f"{document.unique_name}.{document.format}"
        file_deleted = self.firebase.delete_file(filename=filename)
        if not file_deleted:
            return ResponseHandler(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                success=False,
                message=ResponseMessages.FAILED_TO_DELETE_DOCUMENT
            )
        document.delete()   
        return ResponseHandler(
            status=status.HTTP_200_OK,
            success=True,
            message=ResponseMessages.DOCUMENT_DELETED_SUCCESSFULLY
        )
