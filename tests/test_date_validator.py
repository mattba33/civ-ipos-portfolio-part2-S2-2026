import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.date_validator import DateValidator


class TestDateValidator(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(
            DateValidator.validation_date("18-11-26")
        )

    def test_invalid_date(self):
        self.assertFalse(
            DateValidator.validation_date("31-02-26")
        )

    def test_incorrect_format(self):
        self.assertFalse(
            DateValidator.validation_date("18/11/26")
        )

    def test_invalid_day(self):
        self.assertFalse(
            DateValidator.validation_date("32-11-26")
        )

    def test_invalid_month(self):
        self.assertFalse(
            DateValidator.validation_date("18-13-26")
        )

    def test_empty_date(self):
        self.assertFalse(
            DateValidator.validation_date("")
        )

    def test_non_date_input(self):
        self.assertFalse(
            DateValidator.validation_date("hello")
        )


if __name__ == "__main__":
    unittest.main()