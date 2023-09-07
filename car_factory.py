from datetime import datetime

from battery.battery_type.nubbin_battery import NubbinBattery
from battery.battery_type.splinder_battery import SplinderBattery

from tire.tire_types.carrigan_tires import CarriganTires
from tire.tire_types.octoprime_tires import OctoprimeTires

from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine
from car import Car

# NOTE - the specification does NOT specify which cars use which tires so Im just gonna default to use
# the 

class CarFactory():
    # calliope
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        tires = CarriganTires(tire_wear)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(current_date, last_service_date)
        return Car(engine, battery, tires)
    



    # glissade
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        tires = CarriganTires(tire_wear)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(current_date, last_service_date)
        return Car(engine, battery, tires)

    

    # palindrome
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        tires = CarriganTires(tire_wear)
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(current_date, last_service_date)
        return Car(engine, battery, tires)





    # rorschach
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        tires = CarriganTires(tire_wear)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery, tires)
    




    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        tires = CarriganTires(tire_wear)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery, tires)
    
