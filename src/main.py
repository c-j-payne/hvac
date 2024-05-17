# sensor/src/main.py
import asyncio

from viam.module.module import Module
from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

#from ads1115 import ADS1115
from ahs import AHS


async def main():
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered. For an example, see the `__init__.py` file.
    """
    #Registry.register_resource_creator(Sensor.SUBTYPE, ADS1115.MODEL, ResourceCreatorRegistration(ADS1115.new))
    Registry.register_resource_creator(Sensor.SUBTYPE, AHS.MODEL, ResourceCreatorRegistration(AHS.new))

    module = Module.from_args()
    #module.add_model_from_registry(Sensor.SUBTYPE, ADS1115.MODEL)
    module.add_model_from_registry(Sensor.SUBTYPE, AHS.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())