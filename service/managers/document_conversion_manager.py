from service.constants import SupportedFileTypes, ExceptionMessages
from service.utils import logger, validate_conversion_type_and_format
from service.exceptions import BadRequestException
from service.managers.conversion_factories import DocumentFactory, ImageFactory

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
            return DocumentFactory.convert(validated_data)
        elif format_type == 'IMAGE':
            return ImageFactory.convert(validated_data)
        raise BadRequestException(ExceptionMessages.UNKNOWN_FORMAT_TYPE.format(format_type))
