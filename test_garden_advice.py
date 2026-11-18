"""Regression tests for the supplied gardening advice behaviour."""
import unittest
import io
from contextlib import redirect_stdout
from unittest.mock import patch
from garden_advice import get_advice, main, read_choice


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


class InteractiveTests(unittest.TestCase):
    """Verify user input, recovery and cancellation at the CLI boundary."""

    def test_normalized_advice(self):
        """Case and surrounding whitespace do not change matching advice."""
        self.assertEqual(get_advice(" SUMMER ", " Flower "),
                         get_advice("summer", "flower"))

    def test_invalid_then_valid_choice(self):
        """Blank and unsupported entries re-prompt until a valid choice."""
        output = io.StringIO()
        with patch("builtins.input", side_effect=["", "banana", " WINTER "]) as prompt:
            with redirect_stdout(output):
                choice = read_choice("a season", {"summer": "", "winter": ""})
        self.assertEqual(choice, "winter")
        self.assertEqual(prompt.call_count, 3)
        self.assertEqual(output.getvalue().count("Please choose one of:"), 2)

    def test_interactive_advice(self):
        """The CLI uses the entered choices instead of hardcoded defaults."""
        output = io.StringIO()
        with patch("builtins.input", side_effect=["winter", "vegetable"]):
            with redirect_stdout(output):
                main()
        self.assertIn(get_advice("winter", "vegetable"), output.getvalue())
        self.assertNotIn("encourage blooms", output.getvalue())

    def test_invalid_plant_recovery(self):
        """The second prompt also rejects unsupported choices."""
        with patch("builtins.input", side_effect=["tree", "flower"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(read_choice("plant", {"flower": ""}), "flower")

    def test_cancel_input(self):
        """EOF and keyboard interruption at either prompt exit gracefully."""
        for interruption in (EOFError, KeyboardInterrupt):
            for inputs in ([interruption], ["summer", interruption]):
                with self.subTest(interruption=interruption, inputs=inputs):
                    output = io.StringIO()
                    with patch("builtins.input", side_effect=inputs):
                        with redirect_stdout(output):
                            main()
                    self.assertIn("Input cancelled", output.getvalue())


if __name__ == "__main__":
    unittest.main()
