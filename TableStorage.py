import os
from azure.data.tables import TableServiceClient

# Configuración de la tabla 
account_name = "datoscombustibles"
account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY') #ha sido creada anteriormente

#tabla donde se van a guardar todos los datos recogidos
table_name = "datos"

#Comprobamos que exista una variable de entorno con la clave de la cuenta de almacenamiento
if not account_key:
    raise ValueError("Por favor, establece la variable de entorno AZURE_STORAGE_ACCOUNT_KEY antes de ejecutar este script.")

connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

# Crear una instancia del servicio TableServiceClient usando la cadena de conexión
table_service = TableServiceClient.from_connection_string(conn_str=connection_string)

# Crear la tabla
table_client = table_service.create_table_if_not_exists(table_name=table_name)

#Print para asegurarnos que se ha creado la tabla
print(f"Tabla '{table_name}' creada.")



