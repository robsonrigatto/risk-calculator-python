import unittest

from src.constants import fields, values
from src.dtos.context import Context
from src.mappers import risk_mapper

class TestRiskMapper(unittest.TestCase):

    def test_all_conditions(self):
        context = Context({}, 0)
        context.response.auto = values.INELIGIBLE
        context.disability.value = -1
        context.home.value = 2
        context.life.value = 4

        score = risk_mapper.to_score(context)

        self.assertEqual(score.auto, values.INELIGIBLE)
        self.assertEqual(score.disability, values.ECONOMIC)
        self.assertEqual(score.home, values.REGULAR)
        self.assertEqual(score.life, values.RESPONSIBLE)