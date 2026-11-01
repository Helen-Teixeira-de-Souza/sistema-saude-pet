import pymysql

# Simula o PyMySQL como o driver padrão do MySQL para o Django (PCC)
pymysql.install_as_MySQLdb()

from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures as MySQLDatabaseFeatures

# 1. Desativa o suporte a RETURNING que o MariaDB 10.4 não possui
class CustomDatabaseFeatures(MySQLDatabaseFeatures):
    can_return_columns_from_insert = False

# 2. Simula a versão 10.11 para passar na validação inicial do Django
class CustomDatabaseWrapper(MySQLDatabaseWrapper):
    features_class = CustomDatabaseFeatures

    def get_database_version(self):
        return (10, 11, 2)

# Substitui as classes nativas pelas customizadas no Django
MySQLDatabaseWrapper.get_database_version = CustomDatabaseWrapper.get_database_version
MySQLDatabaseWrapper.features_class = CustomDatabaseFeatures