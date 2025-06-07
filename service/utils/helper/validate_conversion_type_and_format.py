from service.constants import (AllowedConversionMapping, ExceptionMessages,
                               SupportedFileTypes)
from service.exceptions import BadRequestException


def validate_conversion_type_and_format(format: str, convert_to_format: str) -> str:
    format_type = None

    if format in SupportedFileTypes.DOCUMENTS.value:
        format_type = 'DOCUMENT'
    elif format in SupportedFileTypes.IMAGES.value:
        format_type = 'IMAGE'
    else:
        raise BadRequestException(ExceptionMessages.UNIDENTIFIED_FORMAT_TYPE.format(format_type))

    allowed_format_object = getattr(AllowedConversionMapping, format_type, None)
    if not allowed_format_object:
        raise BadRequestException(ExceptionMessages.CONVERSION_MAPPING_NOT_FOUND.format(format))
    
    allowed_conversions = allowed_format_object.get(format)
    if not allowed_conversions or convert_to_format not in allowed_conversions:
        raise BadRequestException(ExceptionMessages.CONVERSION_BW_NOT_ALLOWED.format(format, convert_to_format, allowed_conversions))

    return format_type
