from rest_framework.views import APIView

from service.constants import ExceptionMessages, ResponseMessages
from service.exceptions import BadRequestException
from service.models import Documents
from service.utils import Firebase, ResponseHandler


class DeleteAllUserDocumentsView(APIView):
    firebase = Firebase()
    
    def get_queryset(self, user_id):
        return Documents.objects.filter(user_id=user_id)
    
    def post(self, request, user_id):
        documents = self.get_queryset(user_id=user_id)
        if not documents.exists():
            return ResponseHandler(
                success=True,
                message=ExceptionMessages.NO_DOCUMENT_FOUND_FOR_USER.format(user_id)
            ) 
        self._delete_files_from_firebase_and_db(documents)
        return ResponseHandler(
            success=True,
            message=ResponseMessages.ALL_DOCUMENT_DELETED_FOR_USER.format(user_id)
        )

    def _delete_files_from_firebase_and_db(self, documents):
        for document in documents:
            filename = f"{document.unique_name}.{document.format}"
            file_deleted = self.firebase.delete_file(filename=filename)
            if not file_deleted:
                raise BadRequestException(ResponseMessages.FAILED_TO_DELETE_DOCUMENT)
            document.delete()
