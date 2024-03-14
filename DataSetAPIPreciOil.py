import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import DatasetResource, RestResourceDataset, LinkedServiceReference

# Autenticación para Azure, cogemos la id de la suscripcion de una variable de entorno que ha sido
#previamente creada
subscription_id = os.getenv('ID_AZURE_SUSCRIPTION')
#Comprobamos que exista una variable de entorno con el id de la suscripcion
if not subscription_id:
    raise ValueError("Por favor, establece la variable de entorno ID_AZURE_SUSCRIPTION antes de ejecutar este script.")

#Punto de entrada para realizar operaciones
credential = DefaultAzureCredential()
adf_client = DataFactoryManagementClient(credential, subscription_id)

# Datos de configuración
resource_group_name = 'TFGInformatica'
data_factory_name = 'fabricadedatostfg'
linked_service_name = 'ServicioRestAPIPrecioil'

localidades = ['Murcia','Madrid']

for i in localidades:
    # URL relativa (puedes cambiar esto según sea necesario)
    relative_url = i

    # Crear el dataset para el servicio REST
    rest_dataset_name = 'DataSetRest'+i
    rest_dataset = RestResourceDataset(
        linked_service_name=LinkedServiceReference(reference_name=linked_service_name, type='LinkedServiceReference'),
        relative_url=relative_url,
        request_method="GET"
    )

    adf_client.datasets.create_or_update(
        resource_group_name=resource_group_name,
        factory_name=data_factory_name,
        dataset_name=rest_dataset_name,
        dataset=DatasetResource(properties=rest_dataset)
    )

    print(f"Dataset REST '{rest_dataset_name}' creado.")
