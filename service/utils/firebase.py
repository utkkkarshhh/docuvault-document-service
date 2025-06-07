import os
from datetime import timedelta
from uuid import uuid4

import firebase_admin
from firebase_admin import credentials, storage

from service.constants import FirebaseConstants


class Firebase:
    def __init__(self, bucket_name: str = None):
        if not firebase_admin._apps:
            config = FirebaseConstants.get_admin_config()
            cred = credentials.Certificate(config)
            firebase_admin.initialize_app(cred, {
                'storageBucket': bucket_name or os.getenv('FIREBASE_STORAGE_BUCKET')
            })
        self.bucket = storage.bucket()

    def upload_file(self, file, filename, content_type='application/octet-stream') -> str:
        file_extension = os.path.splitext(file.name)[1]
        file_name = f"{filename}{file_extension}"
        blob = self.bucket.blob(file_name)
        blob.upload_from_file(file, content_type=content_type)
        blob.make_public()
        return blob.public_url

    def upload_bytes(self, file_bytes: bytes, filename: str, content_type='application/octet-stream') -> str:
        blob = self.bucket.blob(filename)
        blob.upload_from_string(file_bytes, content_type=content_type)
        blob.make_public()
        return blob.public_url

    def generate_signed_url(self, filename: str, expiration_minutes: int = 15) -> str:
        blob = self.bucket.blob(filename)
        url = blob.generate_signed_url(timedelta(minutes=expiration_minutes))
        return url

    def delete_file(self, filename: str) -> bool:
        blob = self.bucket.blob(filename)
        if blob.exists():
            blob.delete()
            return True
        return False
