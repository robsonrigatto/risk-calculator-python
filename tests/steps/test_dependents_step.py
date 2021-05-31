import unittest

from src.constants import fields
from src.dtos.context import Context
from src.steps import dependents_step

class TestDependentsStep(unittest.TestCase):
    def test_noDependents(self):
        request = { fields.DEPENDENTS: 0 }
        context = Context(request, 0)
        context = dependents_step.do_step(context)

        self.assertEqual(context.disability.value, 0)
        self.assertEqual(context.life.value, 0)

    def test_withDependents(self):
        request = { fields.DEPENDENTS: 1 }
        context = Context(request, 0)
        context = dependents_step.do_step(context)

        self.assertEqual(context.disability.value, 1)
        self.assertEqual(context.life.value, 1)