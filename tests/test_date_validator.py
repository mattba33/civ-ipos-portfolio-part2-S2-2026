import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.date_validator import DateValidator  # noqa: E402


class TestDateValidator(unittest.TestCase):
    """
    Test cases for the DateValidator class.

    Verifies that valid dates are accepted and invalid dates
    or incorrectly formatted inputs are rejected.
    """

    def test_valid_date(self):
        """Test that a correctly formatted and valid date is accepted."""
        self.assertTrue(
            DateValidator.validation_date("18-11-26")
        )

    def test_invalid_date(self):
        """Test that a date that does not exist is rejected."""
        self.assertFalse(
            DateValidator.validation_date("31-02-26")
        )

    def test_incorrect_format(self):
        """Test that dates using an incorrect format are rejected."""
        self.assertFalse(
            DateValidator.validation_date("18/11/26")
        )

    def test_invalid_day(self):
        """Test that dates with an invalid day are rejected."""
        self.assertFalse(
            DateValidator.validation_date("32-11-26")
        )

    def test_invalid_month(self):
        """Test that dates with an invalid month are rejected."""
        self.assertFalse(
            DateValidator.validation_date("18-13-26")
        )

    def test_empty_date(self):
        """Test that an empty date string is rejected."""
        self.assertFalse(
            DateValidator.validation_date("")
        )

    def test_non_date_input(self):
        """Test that non-date text is rejected."""
        self.assertFalse(
            DateValidator.validation_date("hello")
        )


if __name__ == "__main__":
    unittest.main()
