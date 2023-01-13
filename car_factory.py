from car import Car

from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class carFactory(CapuletEngine, SternmanEngine, WilloughbyEngine, NubbinBattery, SplinderBattery):
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        splinder_battery = SplinderBattery(current_date, last_service_date)
        carrigan_tire = CarriganTire(tire_wear)
        calliope = Car(capulet_engine ,splinder_battery, carrigan_tire)
        return calliope
    @staticmethod
    def create_glissade(current_date,  last_service_date, current_mileage, last_service_mileage, tire_wear):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        splinder_battery = SplinderBattery(current_date, last_service_date)
        octoprime_tire = OctoprimeTire(tire_wear)
        glissage = Car(willoughby_engine, splinder_battery, octoprime_tire)
        return glissage
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_wear):
        sternman_engine = SternmanEngine(warning_light_is_on)
        splinder_battery = SplinderBattery(current_date, last_service_date)
        carrigan_tire = CarriganTire(tire_wear)
        glissage = Car(sternman_engine, splinder_battery, carrigan_tire)
        return glissage
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        octoprime_tire = OctoprimeTire(tire_wear)
        rorschach = Car(willoughby_engine, nubbin_battery, octoprime_tire)
        return rorschach
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        carrigan_tire = CarriganTire(tire_wear)
        thovex = Car(capulet_engine, nubbin_battery, carrigan_tire)
        return thovex