import logging
import os

from azure.keyvault import KeyVaultClient
from msrestazure.azure_active_directory import MSIAuthentication

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def _is_app_service():
    return 'APPSETTING_WEBSITE_SITE_NAME' in os.environ

def _get_database_uri():
    if _is_app_service():
        logger.info("Getting Production DB credentials from Keyvault")
        credentials = MSIAuthentication()
        key_vault_client = KeyVaultClient(credentials)

        key_vault_uri = os.environ.get("KEY_VAULT_URI", "PUT YOUR KV BASE URL HERE")
        logger.info("Using KEY_VAULT_URI: {}".format(key_vault_uri))

        result = key_vault_client.get_secret(
            vault_base_url=key_vault_uri,
            secret_name="database-url",
            secret_version="" # empty string -> latest version
        ).value
        logger.info("Secret info: {} {}".format(type(result), len(result))) # XXX TEMP DEBUG
        return result

    else:
        logger.info("Using local Testing Database")
        return TestingConfig.SQLALCHEMY_DATABASE_URI


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    DEBUG = True
    APPINSIGHTS_INSTRUMENTATIONKEY = None
    SECRET_KEY = 'somekey'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = _get_database_uri(),
    APPINSIGHTS_INSTRUMENTATIONKEY = os.environ.get('APPINSIGHTS_INSTRUMENTATIONKEY', TestingConfig.APPINSIGHTS_INSTRUMENTATIONKEY)
    SECRET_KEY = os.environ.get('SECRET_KEY', TestingConfig.SECRET_KEY)
    