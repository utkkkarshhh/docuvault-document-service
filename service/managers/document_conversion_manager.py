from service.constants import SupportedFileTypes, ExceptionMessages
from service.utils import logger, validate_conversion_type_and_format
from service.exceptions import BadRequestException

class DocumentConversionManager:
    """""
        This conversion factory manager dispatches the required converter class for
        the requested document
    """""
    @classmethod
    def initiate_conversion(cls, validated_data):
        format = validated_data.get('format')
        conversion_data = validated_data.get('convert_data')
        convert_to_format = conversion_data.get('format')
        if format not in SupportedFileTypes.get_all_supported_formats():
            logger.info(ExceptionMessages.NOT_SUPPORTED_FORMAT.format(format))
            raise BadRequestException(ExceptionMessages.NOT_SUPPORTED_FORMAT.format(format))
        format_type = validate_conversion_type_and_format(format, convert_to_format)
        if format_type == 'DOCUMENT':
            return DocumentConverter.convert(validated_data)
        elif format_type == 'IMAGE':
            return ImageConverter.convert(validated_data)
        raise BadRequestException(ExceptionMessages.UNKNOWN_FORMAT_TYPE.format(format_type))

class DocumentConverter:
    @classmethod
    def convert(cls, validated_data):
        print('HELOOOOOOOOOOOOOOOOOOOOOOOOOo===========DOCUMENT CLASS=================')

class ImageConverter:
    @classmethod
    def convert(cls, validated_data):
        print('HELOOOOOOOOOOOOOOOOOOOOOOOOOo==========IMAGE CLASS==================')
