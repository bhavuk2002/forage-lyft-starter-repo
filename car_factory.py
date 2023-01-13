from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
class carFactory(CapuletEngine, SternmanEngine, WilloughbyEngine, NubbinBattery, SplinderBattery):
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        splinder_battery = SplinderBattery(current_date, last_service_date)
        calliope = Car(capulet_engine ,splinder_battery)
        return calliope
    @staticmethod
    def create_glissade(current_date,  last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        splinder_battery = SplinderBattery(current_date, last_service_date)
        glissage = Car(willoughby_engine, splinder_battery)
        return glissage
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        sternman_engine = SternmanEngine(warning_light_is_on)
        splinder_battery = SplinderBattery(current_date, last_service_date)
        glissage = Car(sternman_engine, splinder_battery)
        return glissage
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        rorschach = Car(willoughby_engine, nubbin_battery)
        return rorschach
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        thovex = Car(capulet_engine, nubbin_battery)
        return thovex

