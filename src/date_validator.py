import re

from dateutil import parser
from dateutil.parser import ParserError


class DateValidator:
    """
    Validates due dates entered by users.

    Uses python-dateutil to parse dates and regular expressions
    to ensure they follow the required format.
    """

    @staticmethod
    def validation_date(date_string):
        """
        Validate a date string in DD-MM-YY format.

        Args:
            date_string (str): The date string to validate.

        Returns:
            bool: True if the date is valid and correctly formatted,
                  False otherwise.
        """

        if not isinstance(date_string, str):
            return False

        if not re.fullmatch(r"\d{2}-\d{2}-\d{4}", date_string):
            return False

        try:
            parsed_date = parser.parse(date_string, dayfirst=True)
            return parsed_date.strftime("%d-%m-%y") == date_string

        except (ParserError, ValueError, OverflowError):
            return False
