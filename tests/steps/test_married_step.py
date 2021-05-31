import unittest

from src.constants import fields, values
from src.dtos.context import Context
from src.steps import married_step

class TestSum(unittest.TestCase):
    def test_married(self):
        request = { fields.MARITAL_STATUS: values.MARRIED }
        context = Context(request, 0)
        context = married_step.do_step(context)

        self.assertEqual(context.life.value, 1)
        self.assertEqual(context.disability.value, -1)

    def test_single(self):
        request = { fields.MARITAL_STATUS: values.SINGLE}
        context = Context(request, 0)
        context = married_step.do_step(context)

        self.assertEqual(context.life.value, 0)
        self.assertEqual(context.disability.value, 0)