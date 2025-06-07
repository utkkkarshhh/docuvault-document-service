from rest_framework import serializers


class ConversionDataSerializer(serializers.Serializer):
    format = serializers.CharField(required=True)
    size = serializers.IntegerField(required=False)
        
class ConvertDocumentSerializer(serializers.Serializer):
    document_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)
    format = serializers.CharField(required=True)
    convert_data = ConversionDataSerializer()
