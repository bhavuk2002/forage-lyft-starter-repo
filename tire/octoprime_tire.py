from tire import Tire

class octoprime_tire(Tire):
    def __init__(self, tire_health_array):
        self.tire_health_array = tire_health_array
    def needs_service(self):
        sum = 0
        for tire_health in self.tire_health_array:
            sum = sum + tire_health
        if sum >= 3:
            return True
        return False