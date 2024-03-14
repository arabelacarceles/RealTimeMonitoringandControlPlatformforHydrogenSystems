import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import ScheduleTrigger, ScheduleTriggerRecurrence, TriggerResource



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


recurrence = ScheduleTriggerRecurrence(
    frequency='Minute',  # Puede ser Minute, Hour, Day, Week, Month
    interval=1,  # Ejecutar una vez al día
    start_time='2022-01-01T17:00:00Z',  # Hora de inicio en formato UTC
    time_zone='UTC'
)

trigger = ScheduleTrigger(
    recurrence=recurrence
)

trigger_resource = TriggerResource(
    properties=trigger,
    description='Trigger que ejecuta el pipeline diariamente a las 5:00 PM UTC'
)

# Crear o actualizar el trigger en Data Factory
adf_client.triggers.create_or_update(resource_group, data_factory_name, trigger_name, trigger_resource)

