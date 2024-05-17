from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration
#from .ads1115 import ads1115
from .ahs import AHS

#from previous module: 
#Registry.register_resource_creator(Sensor.SUBTYPE, ads1115.MODEL, ResourceCreatorRegistration(ads1115.new, ads1115.validate_config))
Registry.register_resource_creator(Sensor.SUBTYPE, ahs.MODEL, ResourceCreatorRegistration(ahs.new, ahs.validate_config))