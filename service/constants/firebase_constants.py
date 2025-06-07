class FirebaseConstants:
    FIREBASE_CLIENT_CONFIG_KEYS = {
        "apiKey": "FIREBASE_API_KEY",
        "authDomain": "FIREBASE_AUTH_DOMAIN",
        "projectId": "FIREBASE_PROJECT_ID",
        "storageBucket": "FIREBASE_STORAGE_BUCKET",
        "messagingSenderId": "FIREBASE_MESSAGING_SENDER_ID",
        "appId": "FIREBASE_APP_ID",
        "measurementId": "FIREBASE_MEASUREMENT_ID",
    }

    FIREBASE_ADMIN_CONFIG_KEYS = {
        "type": "FIREBASE_TYPE",
        "project_id": "FIREBASE_PROJECT_ID",
        "private_key_id": "FIREBASE_PRIVATE_KEY_ID",
        "private_key": "FIREBASE_PRIVATE_KEY",
        "client_email": "FIREBASE_CLIENT_EMAIL",
        "client_id": "FIREBASE_CLIENT_ID",
        "auth_uri": "FIREBASE_AUTH_URI",
        "token_uri": "FIREBASE_TOKEN_URI",
        "auth_provider_x509_cert_url": "FIREBASE_AUTH_PROVIDER_CERT_URL",
        "client_x509_cert_url": "FIREBASE_CLIENT_CERT_URL",
        "universe_domain": "FIREBASE_UNIVERSE_DOMAIN",
    }

    @classmethod
    def get_client_config(cls) -> dict:
        from service.utils.helper.json_builder import json_builder
        return json_builder(cls.FIREBASE_CLIENT_CONFIG_KEYS)

    @classmethod
    def get_admin_config(cls) -> dict:
        from service.utils.helper.json_builder import json_builder
        return json_builder(cls.FIREBASE_ADMIN_CONFIG_KEYS)
