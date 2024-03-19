import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import DatasetResource, AzureTableDataset

# Autenticación para Azure, cogemos la id de la suscripcion de una variable de entorno que ha sido
#previamente creada
subscription_id = os.getenv('ID_AZURE_SUSCRIPTION')
#Comprobamos que exista una variable de entorno con el id de la suscripcion
if not subscription_id:
    raise ValueError("Por favor, establece la variable de entorno ID_AZURE_SUSCRIPTION antes de ejecutar este script.")

#Punto de entrada para realizar operaciones
credential = DefaultAzureCredential()
adf_client = DataFactoryManagementClient(credential, subscription_id)



resource_group = 'TFGInformatica'
data_factory_name = 'fabricadedatostfg'
linked_service_name = 'ServicioTablaAlmacenamiento'  # Actualiza esto con el nombre de tu Linked Service

localidades = ['Murcia','Madrid','Sevilla','Zaragoza','Oviedo','Palma','SantaCruzdeTenerife', 'Toledo', 'Santander',
               'Valladolid', 'Barcelona', 'Merida', 'SantiagodeCompostela', 'Logronio', 'Valencia', 'Bilbao',
               'Ceuta', 'Melilla']

for i in localidades:
    table_name = 'datosde'+i

    # Crear un Azure Table Storage dataset
    azure_table_dataset = AzureTableDataset(
        linked_service_name={
            "referenceName": linked_service_name,
            "type": "LinkedServiceReference"
        },
        table_name=table_name  # El nombre de tu tabla en Azure Table Storage
    )

    dataset_name = 'DataSetTable'+i
    adf_client.datasets.create_or_update(
        resource_group_name=resource_group,
        factory_name=data_factory_name,
        dataset_name=dataset_name,
        dataset=DatasetResource(properties=azure_table_dataset)
        )

    print(f"Dataset para Azure Table Storage {dataset_name} creado.")
