import unittest

from src.constants import fields, values
from src.dtos.context import Context
from src.steps import mortgaged_step

class TestSum(unittest.TestCase):
    def test_withoutHouse(self):
        request = { }
        context = Context(request, 0)
        context = mortgaged_step.do_step(context)

        self.assertEqual(context.home.value, 0)
        self.assertEqual(context.disability.value, 0)

    def test_ownedHouse(self):
        request = { 
            fields.HOUSE: {
                fields.OWNERSHIP_STATUS: values.OWNED
            } 
        }
        context = Context(request, 0)
        context = mortgaged_step.do_step(context)

        self.assertEqual(context.home.value, 0)
        self.assertEqual(context.disability.value, 0)

    def test_mortgagedHouse(self):
        request = { 
            fields.HOUSE: {
                fields.OWNERSHIP_STATUS: values.MORTGAGED
            } 
        }
        context = Context(request, 0)
        context = mortgaged_step.do_step(context)

        self.assertEqual(context.home.value, 1)
        self.assertEqual(context.disability.value, 1)