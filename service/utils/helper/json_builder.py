import os
from typing import Dict

from service.constants import ExceptionMessages


def json_builder(key_mapping: Dict[str, str]) -> Dict[str, str]:
    result = {}
    for json_key, env_key in key_mapping.items():
        value = os.getenv(env_key)
        if value is None:
            raise EnvironmentError(ExceptionMessages.MISSING_ENV_KEY.format(env_key))
        result[json_key] = value
    return result
