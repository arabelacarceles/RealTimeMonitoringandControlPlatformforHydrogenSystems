import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Autenticación para Azure
credential = DefaultAzureCredential()
subscription_id = os.getenv('ID_AZURE_SUSCRIPTION')

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
