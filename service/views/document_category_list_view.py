from rest_framework import status
from rest_framework.views import APIView

from service.models import DocumentCategoryMaster
from service.serializers import DocumentCategoriesListSerializer
from service.utils import ResponseHandler


class DocumentCategoryListView(APIView):
    serializer_class = DocumentCategoriesListSerializer
    
    def get_queryset(self):
        return DocumentCategoryMaster.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return ResponseHandler(
            status=status.HTTP_200_OK,
            success=True,
            data=serializer.data
        )
