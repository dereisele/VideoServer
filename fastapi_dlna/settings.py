from typing import Dict, Any
import logging

import yaml
from pydantic import BaseSettings

log = logging.getLogger(__name__)


def yaml_config_settings_source(s: BaseSettings) -> Dict[str, Any]:
    with open("application.yaml") as f:
        return yaml.safe_load(f)


class Settings(BaseSettings):
    app_name: str = "Test Server"
    server_ip: str = "127.0.0.1"
    server_port: int = 8080
    discovery_port: int = 1900
    discovery_multicast_addr: str = "239.255.255.250"
    logging: dict = {}

    class Config:
        @classmethod
        def customise_sources(cls,
                              init_settings,
                              env_settings,
                              file_secret_settings
                              ):
            return (
                init_settings,
                yaml_config_settings_source,
                env_settings,
                file_secret_settings
            )


settings = Settings()
