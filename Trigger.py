import os #para poder obtener la variable de entorno
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import ScheduleTrigger, ScheduleTriggerRecurrence, TriggerResource, TriggerPipelineReference, PipelineReference



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

trigger_name = 'Trigger'
pipeline_name = 'Pipeline'

pipeline_reference = TriggerPipelineReference(
    pipeline_reference=PipelineReference(reference_name=pipeline_name, type="PipelineReference"),
    parameters={}
)

recurrence = ScheduleTriggerRecurrence(
    frequency='Hour',  # Puede ser Minute, Hour, Day, Week, Month
    interval=24,  # Ejecutar una vez al día
    start_time='2024-03-01T08:00:00Z',  # Hora de inicio en formato UTC
    end_time='2024-07-01T09:00:00Z',
    time_zone='Romance Standard Time'

)

trigger = ScheduleTrigger(
    recurrence=recurrence,
    pipelines=[pipeline_reference]
)

trigger_resource = TriggerResource(
    properties=trigger
)

# Crear o actualizar el trigger en Data Factory
adf_client.triggers.create_or_update(resource_group, data_factory_name, trigger_name, trigger_resource)

response = adf_client.triggers.begin_start(resource_group, data_factory_name, trigger_name)
response.result()  # Espera a que la operación de inicio finalice

print(f"El trigger '{trigger_name}' ha sido activado.")

