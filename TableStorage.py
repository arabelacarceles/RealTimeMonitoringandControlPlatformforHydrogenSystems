import os
from azure.data.tables import TableServiceClient

#Autenticacion de la cuenta de almacenamiento que queremos usar
account_name = "datoscombustibles"
account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY') #ha sido creada anteriormente
#Comprobamos que exista una variable de entorno con la clave de la cuenta de almacenamiento
if not account_key:
    raise ValueError("Por favor, establece la variable de entorno AZURE_STORAGE_ACCOUNT_KEY antes de ejecutar este script.")

# Crear una instancia del servicio TableServiceClient usando la cadena de conexión
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
table_service = TableServiceClient.from_connection_string(conn_str=connection_string)

localidades = ['Murcia','Madrid','Sevilla','Zaragoza','Oviedo','Palma','SantaCruzdeTenerife', 'Toledo', 'Santander',
               'Valladolid', 'Barcelona', 'Merida', 'SantiagodeCompostela', 'Logronio', 'Valencia', 'Bilbao',
               'Ceuta', 'Melilla']
for i in localidades:
    
    #Configuracion de la tabla
    table_name = "datosde"+i
    # Creación de la tabla
    table_client = table_service.create_table_if_not_exists(table_name=table_name)
    #Print para asegurarnos que se ha creado la tabla
    print(f"Tabla '{table_name}' creada.")





