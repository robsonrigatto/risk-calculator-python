import unittest

from src.constants import fields, values
from src.dtos.context import Context
from src.steps import vehicle_step

class TestSum(unittest.TestCase):
    def test_withoutVehicle(self):
        request = { }
        context = Context(request, 0)
        context = vehicle_step.do_step(context)

        self.assertEqual(context.auto.value, 0)

    def test_oldVehicle(self):
        request = { 
            fields.VEHICLE: {
                fields.YEAR: 2000
            } 
        }
        context = Context(request, 0)
        context = vehicle_step.do_step(context)

        self.assertEqual(context.auto.value, 0)

    def test_newVehicle(self):
        request = { 
            fields.VEHICLE: {
                fields.YEAR: 2021
            } 
        }
        context = Context(request, 0)
        context = vehicle_step.do_step(context)

        self.assertEqual(context.auto.value, 1)