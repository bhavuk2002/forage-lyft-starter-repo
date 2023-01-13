from serviceable import serviceable
class Car(serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery
    def needs_service(self):
        return self.engine.need_services() or self.battery.need_services()