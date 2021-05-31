import unittest

from src.constants import fields, values
from src.dtos.context import Context
from src.services import risk_service

class TestRiskService(unittest.TestCase):
    def test_withoutHouseAndVehicle(self):
        request = { 
            fields.RISK_QUESTIONS: [0,1,0], 
            fields.AGE : 35,
            fields.DEPENDENTS: 2,
            fields.INCOME: 0,
            fields.MARITAL_STATUS: values.MARRIED
        }
        score = risk_service.calculate(request)

        self.assertEqual(score.life, values.REGULAR)
        self.assertEqual(score.auto, values.INELIGIBLE)

    def test_withHouseAndVehicle(self):
        request = { 
            fields.RISK_QUESTIONS: [0,1,0], 
            fields.AGE : 35,
            fields.DEPENDENTS: 2,
            fields.INCOME: 0,
            fields.MARITAL_STATUS: values.MARRIED,
            fields.HOUSE: {
                fields.OWNERSHIP_STATUS: values.OWNED
            },
            fields.VEHICLE: {
                fields.YEAR: 2020
            }
        }
        score = risk_service.calculate(request)

        self.assertEqual(score.life, values.REGULAR)
        self.assertEqual(score.auto, values.REGULAR)

    def test_withIncome(self):
        request = { 
            fields.RISK_QUESTIONS: [0,0,0], 
            fields.AGE : 35,
            fields.DEPENDENTS: 2,
            fields.INCOME: 200001,
            fields.MARITAL_STATUS: values.MARRIED,
            fields.HOUSE: {
                fields.OWNERSHIP_STATUS: values.OWNED
            },
            fields.VEHICLE: {
                fields.YEAR: 2020
            }
        }
        score = risk_service.calculate(request)

        self.assertEqual(score.life, values.ECONOMIC)