from rest_framework.views import APIView

from service.exceptions import BadRequestException
from service.managers import DocumentConversionManager
from service.serializers import ConvertDocumentSerializer
from service.utils import CommonUtils, ResponseHandler


class ConvertDocumentView(APIView):
    serializer_class = ConvertDocumentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise BadRequestException(CommonUtils.handle_serializer_error(serializer.errors))
        validated_data = serializer.validated_data
        response = DocumentConversionManager.initiate_conversion(validated_data)
        return ResponseHandler(
            success=True,
            data=response
        )
