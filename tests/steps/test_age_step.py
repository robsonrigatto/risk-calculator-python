import unittest

from src.constants import fields, values
from src.dtos.context import Context
from src.steps import age_step

class TestAgeStep(unittest.TestCase):
    def test_above60years(self):
        request = { fields.AGE: 63 }
        context = Context(request, 0)
        context = age_step.do_step(context)

        self.assertEqual(context.response.disability, values.INELIGIBLE)
        self.assertEqual(context.response.life, values.INELIGIBLE)

    def test_60years(self):
        request = { fields.AGE: 60 }
        context = Context(request, 0)
        context = age_step.do_step(context)

        self.assertIsNone(context.response.disability)
        self.assertIsNone(context.response.life)

    def test_30years(self):
        request = { fields.AGE: 30 }
        context = Context(request, 0)
        context = age_step.do_step(context)

        self.assertEqual(context.disability.value, -1)
        self.assertEqual(context.life.value, -1)

    def test_below30years(self):
        request = { fields.AGE: 25 }
        context = Context(request, 0)
        context = age_step.do_step(context)

        self.assertEqual(context.disability.value, -2)
        self.assertEqual(context.life.value, -2)