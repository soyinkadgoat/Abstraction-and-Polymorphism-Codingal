from abc import ABC, abstractmethod

class SmartDevice(ABC):

    @abstractmethod

    def operate(self):
        pass

class SmartLight(SmartDevice):

    def operate(self):
        print("SmartLight is turned ON")

class SmartFan(SmartDevice):

    def operate(self):
        print("Smartfan is rotating")


class SmartTV(SmartDevice):

    def operate(self):
        print("SmartTV is playing")


devices = [SmartLight(), SmartFan(), SmartTV()]

for device in devices:
    device.operate()