from service.exceptions import BadRequestException

class ImageFactory:
    @classmethod
    def convert(cls, validated_data):
        format = validated_data.get('format')
        conversion_data = validated_data.get('convert_data')
        convert_to_format = conversion_data.get('format')

        match (format, convert_to_format):
            case ('jpeg', 'jpg'):
                return cls.convert_jpeg_to_jpg(validated_data)
            case ('jpeg', 'png'):
                return cls.convert_jpeg_to_png(validated_data)
            case ('jpeg', 'svg'):
                return cls.convert_jpeg_to_svg(validated_data)
            case ('jpg', 'jpeg'):
                return cls.convert_jpg_to_jpeg(validated_data)
            case ('jpg', 'png'):
                return cls.convert_jpg_to_png(validated_data)
            case ('jpg', 'svg'):
                return cls.convert_jpg_to_svg(validated_data)
            case ('png', 'jpeg'):
                return cls.convert_png_to_jpeg(validated_data)
            case ('png', 'jpg'):
                return cls.convert_png_to_jpg(validated_data)
            case ('png', 'svg'):
                return cls.convert_png_to_svg(validated_data)
            case ('svg', 'jpeg'):
                return cls.convert_svg_to_jpeg(validated_data)
            case ('svg', 'jpg'):
                return cls.convert_svg_to_jpg(validated_data)
            case ('svg', 'png'):
                return cls.convert_svg_to_png(validated_data)
            case _:
                raise BadRequestException(f"Unsupported image conversion: {format} to {convert_to_format}")
            
    @classmethod
    def convert_jpeg_to_jpg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_jpeg_to_png(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_jpeg_to_svg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_jpg_to_jpeg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_jpg_to_png(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_jpg_to_svg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_png_to_jpeg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_png_to_jpg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_png_to_svg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_svg_to_jpeg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_svg_to_jpg(cls, data): return f"New IMAGE FILE"

    @classmethod
    def convert_svg_to_png(cls, data): return f"New IMAGE FILE"
