"""Module to test given examples from part 2."""
import unittest

import fuel_calculator


class TestFuelCalculator(unittest.TestCase):
    """Class to test basic cases for fuel requirements."""

    def test_fuel_mass_complete_14(self):
        """Check fuel_complete(14) -> 2."""
        self.assertEqual(fuel_calculator.get_fuel_needed_complete(14), 2)

    def test_fuel_mass_complete_1969(self):
        """Check fuel_complete(1969) -> 966."""
        self.assertEqual(fuel_calculator.get_fuel_needed_complete(1969), 966)

    def test_fuel_mass_complete_100756(self):
        """Check fuel_complete(100756) -> 50346."""
        self.assertEqual(
            fuel_calculator.get_fuel_needed_complete(100756), 50346
        )
