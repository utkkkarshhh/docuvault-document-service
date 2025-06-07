from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from service.serializers import DocumentObjectSerializer
from service.models import Documents
from service.utils import ResponseHandler
from service.constants import ResponseMessages

class UserDocumentListView(APIView):
    serializer_class = DocumentObjectSerializer

    def get_queryset(self, user_id):
        return Documents.objects.filter(user_id=user_id)

    def get(self, request, user_id: int):
        queryset = self.get_queryset(user_id)
        
        if not queryset.exists():
            return ResponseHandler(
                success=True,
                data=[],
                message=ResponseMessages.NO_DOCUMENTS_FOUND.format(user_id),
                status=status.HTTP_200_OK
            )

        serializer = self.serializer_class(queryset, many=True)
        return ResponseHandler(
            success=True,
            data=serializer.data,
            message=ResponseMessages.DOCUMENTS_RETRIEVED_SUCCESSFULLY,
            status=status.HTTP_200_OK
        )
