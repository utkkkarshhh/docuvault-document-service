from enum import Enum
from typing import List

class Constants:
    pass

class SupportedFileTypes(Enum):
    DOCUMENTS = ["pdf", "doc", "docx", "xls", "xlsx", "csv"]
    IMAGES = ["jpeg", "jpg", "png", "svg"]

    @classmethod
    def get_all_document_formats(cls) -> List[str]:
        return cls.DOCUMENTS.value

    @classmethod
    def get_all_image_formats(cls) -> List[str]:
        return cls.IMAGES.value

    @classmethod
    def get_all_supported_formats(cls) -> List[str]:
        return cls.DOCUMENTS.value + cls.IMAGES.value

class AllowedConversionMapping:
    DOCUMENT = {
        'pdf' : ["doc", "docx"],
        'xls' : ["csv", "xlsx"],
        'xlsx' : ["csv", "xls"],
        'csv' : ["xls", "xlsx"],
        'doc' : ["pdf", "docx"],
        'docx' : ["pdf", "doc"],
    }
    IMAGE = {
        'jpeg' : ["jpg", "png", "svg"],
        'jpg' : ["jpeg", "png", "svg"],
        'png' : ["jpeg", "jpg", "svg"],
        'svg' : ["jpeg", "jpg", "png"],
    }
