import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Autenticación para Azure, cogemos la id de la suscripcion de una variable de entorno que ha sido
#previamente creada
credential = DefaultAzureCredential()
subscription_id = os.getenv('ID_AZURE_SUSCRIPTION')

#Comprobamos que exista una variable de entorno con el id de la suscripcion
if not subscription_id:
    raise ValueError("Por favor, establece la variable de entorno ID_AZURE_SUSCRIPTION antes de ejecutar este script.")

# Crear cliente de gestión de recursos en función de la suscripcion
resource_client = ResourceManagementClient(credential, subscription_id)

#Nombre de recursos + Region
resource_group_name = 'TFGInformatica'
location = 'West Europe'

# Crear el grupo de recursos
resource_group = resource_client.resource_groups.create_or_update(
    resource_group_name,
    {
        'location': location
    }
)

#Print para asegurarnos que se ha creado el grupo de recursos
print(f"Grupo de recursos '{resource_group_name}' creado en la ubicación '{location}'.")
