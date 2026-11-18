import re

from dateutil import parser
from dateutil.parser import ParserError


class DateValidator:

    @staticmethod
    def validation_date(date_string):

        if not isinstance(date_string, str):
            return False
        
        if not re.fullmatch(r"\d{2}-\d{2}-\d{2}", date_string):
            return False
        
        try:
            parser.parse(date_string, dayfirst=True)
            return True
        
        except (ParserError, ValueError, OverflowError):
            return False