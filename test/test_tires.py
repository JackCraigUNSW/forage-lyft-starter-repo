import unittest
from datetime import datetime

from tire.tire_types.carrigan_tires import CarriganTires
from tire.tire_types.octoprime_tires import OctoprimeTires

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tires = CarriganTires([0.99]*4)
        self.assertTrue(tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        tires = CarriganTires([0.8]*4)
        self.assertFalse(tires.needs_service())




class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tires = OctoprimeTires([0.9]*4)
        self.assertTrue(tires.needs_service())

    def test_tire_should_not_be_serviced(self):
        tires = OctoprimeTires([0.01]*4)
        self.assertFalse(tires.needs_service())