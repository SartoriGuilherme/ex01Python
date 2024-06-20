import unittest

from IndustrializedProduct import IndustrializedProduct
from AgriculturalProduct import AgriculturalProduct


class TestProject(unittest.TestCase):

    def test_IndustrializedProduct25(self):
        industrializedProduct25 = IndustrializedProduct("Chapa", 25.0, 3.0, 0.35, 1.12, 1.05)
        self.assertAlmostEqual(99.834, industrializedProduct25.getFinalPrice())

    def test_IndustrializedProduct150(self):
        industrializedProduct150 = IndustrializedProduct("Colher", 5, 150, 0.30, 1.12, 1.05)
        self.assertAlmostEqual(1019.61, industrializedProduct150.getFinalPrice())

    def test_IndustrializedProduct250(self):
        industrializedProduct250 = IndustrializedProduct("Colher", 5, 150, 0.30, 1.12, 1.05)
        self.assertAlmostEqual(1019.61, industrializedProduct250.getFinalPrice())

    def test_AgriculturalProduct3(self):
        agriculturalProduct3 = AgriculturalProduct("Laranja", 3.45, 3, 0.10)
        self.assertAlmostEqual(11.478, agriculturalProduct3.getFinalPrice())

    def test_AgriculturalProduct101(self):
        agriculturalProduct101 = AgriculturalProduct("Abacate", 20.0, 100.01, 0.08)
        self.assertAlmostEqual(2108.2108, agriculturalProduct101.getFinalPrice())

    def test_AgriculturalProduct734(self):
        agriculturalProduct734 = AgriculturalProduct("Melancia", 1.99, 734.0, 0.05)
        self.assertAlmostEqual(1548.4831, agriculturalProduct734.getFinalPrice())
