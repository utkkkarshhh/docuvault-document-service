from service.exceptions import BadRequestException

class DocumentFactory:
    @classmethod
    def convert(cls, validated_data):
        format = validated_data.get('format')
        conversion_data = validated_data.get('convert_data')
        convert_to_format = conversion_data.get('format')

        match (format, convert_to_format):
            case ('pdf', 'doc'):
                return cls.convert_pdf_to_doc(validated_data)
            case ('pdf', 'docx'):
                return cls.convert_pdf_to_docx(validated_data)
            case ('xls', 'csv'):
                return cls.convert_xls_to_csv(validated_data)
            case ('xls', 'xlsx'):
                return cls.convert_xls_to_xlsx(validated_data)
            case ('xlsx', 'csv'):
                return cls.convert_xlsx_to_csv(validated_data)
            case ('xlsx', 'xls'):
                return cls.convert_xlsx_to_xls(validated_data)
            case ('csv', 'xls'):
                return cls.convert_csv_to_xls(validated_data)
            case ('csv', 'xlsx'):
                return cls.convert_csv_to_xlsx(validated_data)
            case ('doc', 'pdf'):
                return cls.convert_doc_to_pdf(validated_data)
            case ('doc', 'docx'):
                return cls.convert_doc_to_docx(validated_data)
            case ('docx', 'pdf'):
                return cls.convert_docx_to_pdf(validated_data)
            case ('docx', 'doc'):
                return cls.convert_docx_to_doc(validated_data)
            case _:
                raise BadRequestException(f"Unsupported document conversion: {format} to {convert_to_format}")

    @classmethod
    def convert_pdf_to_doc(cls, data):
        return f"New DOCUMENT FILE"

    @classmethod
    def convert_pdf_to_docx(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_xls_to_csv(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_xls_to_xlsx(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_xlsx_to_csv(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_xlsx_to_xls(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_csv_to_xls(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_csv_to_xlsx(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_doc_to_pdf(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_doc_to_docx(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_docx_to_pdf(cls, data): return f"New DOCUMENT FILE"

    @classmethod
    def convert_docx_to_doc(cls, data): return f"New DOCUMENT FILE"