class ResponseMessages:
    HEALTHY_SERVICE = "Document Service is healthy and running"
    FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully"
    FORMAT_NOT_SUPPORTED = "File format not supported"
    DOCUMENTS_RETRIEVED_SUCCESSFULLY = "Retrieved user documents"
    NO_DOCUMENTS_FOUND = "No documents found for user id {}"
    NO_DOCUMENT_FOUND_FOR_ID = "No document with id {} found for user id {}"
    DOCUMENT_DELETED_SUCCESSFULLY = "Document deleted successfully"
    FAILED_TO_DELETE_DOCUMENT = "Failed to delete the document"
    FILE_FETCHED_SUCCESSFULLY = 'File fetched successfully'
    DOCUMENT_DOES_NOT_BELONG_TO_USER = "This document does not belong to the user"

class HTTPResponseMessages:
    HTTP_REQUEST_ERROR = "Error while making HTTP request"
    STATUS_CODE_ERROR = "Unexpected status code received"
    AUTHENTICATION_ERROR = "Authentication failed. Please check your credentials"
    INVALID_METHOD = "Invalid HTTP method used for this endpoint."
    UNSUPPORTED_DATA = "Unsupported media type"
    UNACCEPTABLE_DATA = "Unacceptable data"
    
class ExceptionMessages:
    DATA_NOT_AVAILABLE = "Data not available"
    DOES_NOT_EXIST = "Resource does not exist"
    SOMETHING_WENT_WRONG = "Something went wrong"
    MISSING_ENV_KEY = "Missing environment variable: {}"
    NOT_SUPPORTED_FORMAT = "{} is not a supported format"
    CONVERSION_BW_NOT_ALLOWED = "Conversion from {} to {} is not supported, valid options are {}"
    UNKNOWN_FORMAT_TYPE = "{} is an unknown format type"
    UNIDENTIFIED_FORMAT_TYPE = "{} is an unidentified format. Please try after some time."
    CONVERSION_MAPPING_NOT_FOUND = "Conversion mapping not found for format {}"
