import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters

# Configuración de la cuenta de almacenamiento
subscription_id = os.getenv('ID_AZURE_SUSCRIPTION')
resource_group = 'TFGInformatica'
storage_account_name = 'datoscombustibles'  
location = 'West Europe'

#Comprobamos que exista una variable de entorno con el id de la suscripcion
if not subscription_id:
    raise ValueError("Por favor, establece la variable de entorno ID_AZURE_SUSCRIPTION antes de ejecutar este script.")


# Autenticación para Azure, cogemos la id de la suscripcion de una variable de entorno que ha sido
#previamente creada
credential = DefaultAzureCredential()
storage_client = StorageManagementClient(credential, subscription_id)

# Parámetros de la cuenta de almacenamiento
parameters = StorageAccountCreateParameters(
    sku={'name': 'Standard_LRS'},
    kind='StorageV2',
    location=location
)

# Creacion de la cuenta de almacenamiento
storage_account = storage_client.storage_accounts.begin_create(
    resource_group_name=resource_group,
    account_name=storage_account_name,
    parameters=parameters
).result()

#Print para asegurarnos que se ha creado la cuenta de almacenamiento
print(f"Storage account {storage_account_name} creado con éxito.")
