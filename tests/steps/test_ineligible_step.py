import unittest

from src.constants import fields, values
from src.dtos.context import Context
from src.steps import ineligible_step

class TestSum(unittest.TestCase):
    def test_allNullFields(self):
        request = { fields.INCOME: 0 }
        context = Context(request, 0)
        context = ineligible_step.do_step(context)

        self.assertEqual(context.response.auto, values.INELIGIBLE)
        self.assertEqual(context.response.disability, values.INELIGIBLE)
        self.assertEqual(context.response.home, values.INELIGIBLE)

    def test_allFilledFields(self):
        request = { 
            fields.INCOME: 200000, 
            fields.HOUSE: {
                fields.OWNERSHIP_STATUS: values.OWNED
            },
            fields.VEHICLE: {
                fields.YEAR: 2020
            }
        }
        context = Context(request, 0)
        context = ineligible_step.do_step(context)

        self.assertIsNone(context.response.auto)
        self.assertIsNone(context.response.disability)
        self.assertIsNone(context.response.home)