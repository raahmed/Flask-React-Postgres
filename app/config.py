import os

from azure.keyvault import KeyVaultClient
from msrestazure.azure_active_directory import MSIAuthentication

def _get_database_uri():

    if "APPSETTING_WEBSITE_SITE_NAME" in os.environ:
        credentials = MSIAuthentication(resource='https://vault.azure.net')
        key_vault_client = KeyVaultClient(credentials)

        key_vault_uri = os.environ.get("KEY_VAULT_URI")

        return key_vault_client.get_secret(
            key_vault_uri,
            "database-url",
            ""
        )
    else:
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
    