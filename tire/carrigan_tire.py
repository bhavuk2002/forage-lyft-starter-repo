from tire import Tire

class carrigan_tire(Tire):
    def __init__(self, tire_health_array):
        self.tire_health_array = tire_health_array
    def needs_service(self):
        for tire_health in self.tire_health_array:
            if tire_health >= 0.9:
                return True
        return False