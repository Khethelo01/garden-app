"""Regression tests for the supplied gardening advice behaviour."""
import unittest
from garden_advice import get_advice


class AdviceTests(unittest.TestCase):
    """Check supported combinations and original fallback messages."""

    def test_starter_output(self):
        """The summer/flower example keeps its exact output."""
        self.assertEqual(get_advice("summer", "flower"),
                         "Water your plants regularly and provide some shade.\n"
                         "Use fertiliser to encourage blooms.")

    def test_winter_vegetable(self):
        """Both winter and vegetable guidance appear."""
        self.assertEqual(get_advice("winter", "vegetable"),
                         "Protect your plants from frost with covers.\n"
                         "Keep an eye out for pests!")

    def test_unknown_season(self):
        """An unsupported season retains known plant guidance."""
        self.assertEqual(get_advice("unknown", "flower"),
                         "No advice for this season.\n"
                         "Use fertiliser to encourage blooms.")

    def test_unknown_plant(self):
        """An unsupported plant retains known seasonal guidance."""
        self.assertEqual(get_advice("winter", "unknown"),
                         "Protect your plants from frost with covers.\n"
                         "No advice for this type of plant.")

    def test_unknown_values(self):
        """Unknown choices use both fallback sentences."""
        self.assertEqual(get_advice("unknown", "unknown"),
                         "No advice for this season.\n"
                         "No advice for this type of plant.")


if __name__ == "__main__":
    unittest.main()
