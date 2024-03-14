from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *

# Autenticación
credential = DefaultAzureCredential()

# Parámetros - reemplaza estos con tus propios valores
subscription_id = 'a4dbf847-6629-4e01-a0ae-492acf098e95'
resource_group = 'TFG'
location = 'West Europe'
data_factory_name = 'ejemplo3'

# Cliente de gestión de recursos para operaciones de grupo de recursos
resource_client = ResourceManagementClient(credential, subscription_id)

# Crea o actualiza el grupo de recursos
rg_params = {'location': location}
resource_client.resource_groups.create_or_update(resource_group, rg_params)

# Cliente de Data Factory
adf_client = DataFactoryManagementClient(credential, subscription_id)

# Crea o actualiza la instancia de Data Factory
df_resource = Factory(location=location)
data_factory = adf_client.factories.create_or_update(resource_group, data_factory_name, df_resource)

print(f"Data Factory '{data_factory_name}' ha sido creada o actualizada.")
