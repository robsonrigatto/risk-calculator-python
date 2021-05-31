import unittest

from src.constants import fields
from src.dtos.context import Context
from src.steps import income_step

class TestIncomeStep(unittest.TestCase):
    def test_noIncome(self):
        request = { fields.INCOME: 0 }
        context = Context(request, 0)
        context = income_step.do_step(context)

        self.assertEqual(context.life.value, 0)

    def test_withLimitIncome(self):
        request = { fields.INCOME: 200000 }
        context = Context(request, 0)
        context = income_step.do_step(context)

        self.assertEqual(context.life.value, 0)

    def test_withAboveIncome(self):
        request = { fields.INCOME: 200001 }
        context = Context(request, 0)
        context = income_step.do_step(context)

        self.assertEqual(context.life.value, -1)