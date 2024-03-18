import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import (
    PipelineResource, 
    CopyActivity, 
    DatasetReference,
    TabularTranslator,
    CopySource,
    CopySink
)

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

actividades_copia=[]
localidades = ['Murcia','Madrid','Sevilla','Zaragoza','Oviedo','Palma','SantaCruzdeTenerife', 'Toledo', 'Santander',
               'Valladolid', 'Barcelona', 'Merida', 'SantiagodeCompostela', 'Logronio', 'Pamplona', 'Valencia', 'Vitoria',
               'Ceuta', 'Melilla']
for i in localidades:
    rest_dataset_name = 'DataSetRest'+i  # Nombre del dataset REST
    table_storage_dataset_name = 'DataSetTable'+i  # Nombre del dataset de Table Storage

    # Definición de la actividad de copia
    copy_activity = CopyActivity(
        name='ActividadDeCopia'+i,
        inputs=[DatasetReference(reference_name=rest_dataset_name,type='DatasetReference')],
        outputs=[DatasetReference(reference_name=table_storage_dataset_name,type='DatasetReference')],
        source=(DatasetReference(reference_name=rest_dataset_name,type='DatasetReference')),  # Usamos un CopySource genérico
        sink=(DatasetReference(reference_name=table_storage_dataset_name,type='DatasetReference')),  # Usamos un CopySink genérico
        translator=TabularTranslator()
        # Aquí puedes agregar opciones de configuración adicionales para la actividad de copia.
    )
    
    actividades_copia.append(copy_activity)
    

# Creación del pipeline
pipeline = PipelineResource(
    activities=actividades_copia,
)

pipeline_name = 'Pipeline'
adf_client.pipelines.create_or_update(
    resource_group_name=resource_group,
    factory_name=data_factory_name,
    pipeline_name=pipeline_name,
    pipeline=pipeline
)

print(f"Pipeline {pipeline_name} ha sido creado.")
