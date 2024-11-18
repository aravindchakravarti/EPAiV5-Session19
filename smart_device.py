from typing import Any, Callable

class SmartDevice:
    ''' Smart device class which manages all the smart devices connected. '''

    device_count = 0

    def __init__(self, part_name: str, part_model: str, part_online: bool = False):
        ''' Initializes the object with 
        
        Params:
        part_name:      A string representing IOT device Part Name
        part_model:     A string representing IOT device Model Number
        part_online:    Status of the IOT device (default is False)

        Returns:
        None
        '''
        if not isinstance(part_name, str):
            raise TypeError("part_name should be of type 'str'")
        if not isinstance(part_model, str):
            raise TypeError("part_model should be of type 'str'")
        if not isinstance(part_online, bool):
            raise TypeError("part_online should be of type 'bool'")
        
        self.device_name = part_name
        self.model_number = part_model
        self.is_online = part_online
        self.status = {}
        SmartDevice.device_count += 1

    def update_status(self, param: str, value: Any) -> None:
        ''' Updates the status of the connected device. '''
        self.status[param] = value

    def get_status(self, param: str) -> Any:
        ''' Gets the status of a particular parameter of a smart device. '''
        try:
            return self.status[param]
        except KeyError:
            return "Attribute not found"

    def toggle_online(self) -> None:
        ''' Toggles the device's online status between True and False. '''
        self.is_online = not self.is_online

    def reset(self) -> None:
        ''' Deletes all status parameters of the smart device. '''
        self.status = {}

    def __call__(self) -> str:
        ''' Makes the object callable and returns basic device information. '''
        return f"{self.device_name} (Model: {self.model_number})"

    @property
    def device_info(self) -> Callable[[], str]:
        ''' Provides device information as a callable function. '''
        if hasattr(self, "_custom_device_info"):
            return self._custom_device_info
        else:
            def default_info() -> str:
                return f"Device Name: {self.device_name}, Model: {self.model_number}, Online: {self.is_online}"
            return default_info 
    
    @device_info.setter
    def device_info(self, custom_callable: Callable[[], str]) -> None:
        ''' Sets a custom callable for the device information. '''
        if not callable(custom_callable):
            raise TypeError("device_info must be a callable")
        self._custom_device_info = custom_callable