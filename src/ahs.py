import time
import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional, Sequence, List, cast
from viam.components.sensor import Sensor
from viam.logging import getLogger
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily
from viam.utils import ValueTypes, struct_to_dict
LOGGER = getLogger(__name__)

class SerialSensor(Sensor):
    MODEL: ClassVar[Model] = Model(ModelFamily("chris", "i2c-sensor"), "ahs")
    channel: int 
    

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        return []

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> "SerialSensor":
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    def __init__(self, name: str):
        super().__init__(name)

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        try:
            self.channel = int(config.attributes.fields.get("channel", {}).number_value or 0)

    async def close(self):
        return
      

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
              
        return ""

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        LOGGER.info("getreading")

        return([])