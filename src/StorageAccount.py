import os #para poder obtener la variable de entorno
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters

# Autenticación para Azure, cogemos la id de la suscripcion de una variable de entorno que ha sido
#previamente creada
subscription_id = os.getenv('ID_AZURE_SUSCRIPTION')
#Comprobamos que exista una variable de entorno con el id de la suscripcion
if not subscription_id:
    raise ValueError("Por favor, establece la variable de entorno ID_AZURE_SUSCRIPTION antes de ejecutar este script.")

# Punto de entrada para realizar operaciones
credential = DefaultAzureCredential()
storage_client = StorageManagementClient(credential, subscription_id)

# Configuración de la cuenta de almacenamiento
resource_group = 'TFGInformatica'
storage_account_name = 'datoscombustibles'  
location = 'West Europe'


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
