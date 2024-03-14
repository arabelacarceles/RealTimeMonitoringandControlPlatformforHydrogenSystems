import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import LinkedServiceResource, AzureTableStorageLinkedService, DatasetResource, AzureTableDataset

# Autenticación para Azure, cogemos la id de la suscripcion de una variable de entorno que ha sido
#previamente creada
subscription_id = os.getenv('ID_AZURE_SUSCRIPTION')
#Comprobamos que exista una variable de entorno con el id de la suscripcion
if not subscription_id:
    raise ValueError("Por favor, establece la variable de entorno ID_AZURE_SUSCRIPTION antes de ejecutar este script.")

account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')
if not account_key:
    raise ValueError("Por favor, establece la variable de entorno AZURE_STORAGE_ACCOUNT_KEY antes de ejecutar este script.")

#Punto de entrada para realizar operaciones
credential = DefaultAzureCredential()
adf_client = DataFactoryManagementClient(credential, subscription_id)

#Configuracion del servicio 
resource_group = 'TFGInformatica'
data_factory_name = 'fabricadedatostfg'
storage_account_name = 'datoscombustibles'

# Crear Linked Service para Azure Table Storage
azure_table_storage_linked_service = AzureTableStorageLinkedService(
    connection_string=f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
)

ls_name = 'ServicioTablaAlmacenamiento'
adf_client.linked_services.create_or_update(
    resource_group_name=resource_group,
    factory_name=data_factory_name,
    linked_service_name=ls_name,
    linked_service=LinkedServiceResource(properties=azure_table_storage_linked_service)
)

print(f"Linked Service {ls_name} creado.")

