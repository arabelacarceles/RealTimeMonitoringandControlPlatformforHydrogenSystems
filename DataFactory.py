import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *

# Autenticación para Azure, cogemos la id de la suscripcion de una variable de entorno que ha sido
#previamente creada
subscription_id = os.getenv('ID_AZURE_SUSCRIPTION')
#Comprobamos que exista una variable de entorno con el id de la suscripcion
if not subscription_id:
    raise ValueError("Por favor, establece la variable de entorno ID_AZURE_SUSCRIPTION antes de ejecutar este script.")

# Punto de entrada para realizar operaciones tanto del grupo de recursos como de la fabrica
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
adf_client = DataFactoryManagementClient(credential, subscription_id)

# Parámetros grupo de recursos
resource_group = 'TFGInformatica'
location = 'West Europe'



#Nos aseguramos que el grupo de recursos al que va a estar asociado la fabrica este configurado
#correctamente y de acuerdo a la configuracion que se va a hacer de la fabrica
rg_params = {'location': location}
resource_client.resource_groups.create_or_update(resource_group, rg_params)


# Creaacion de la fabrica de datos
data_factory_name = 'fabricadedatostfg'
df_resource = Factory(location=location)
data_factory = adf_client.factories.create_or_update(resource_group, data_factory_name, df_resource)

#Print para asegurarnos que se ha creado la fabrica
print(f"Data Factory '{data_factory_name}' ha sido creada.")
