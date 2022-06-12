import re

SECONDS_AND_MINUTES_REGEX_EXPRESSION = "^([1-5]?\\d,)*[1-5]?\\d$|^[1-5]?\\d\\/[1-5]?\\d$|^[1-5]?\\d$|^\\*\\/[" \
                                       "1-5]?\\d$|^\\*$"
SECONDS_AND_MINUTES_RANGE_REGEX_EXPRESSION = "^[1-5]?\\d-[1-5]?\\d$"
HOURS_REGEX_EXPRESSION = "^\\b(\\d|1\\d|2[0-3])\\b$|^((\\b(\\d|1\\d|2[0-3])\\b),)*(\\b(\\d|1\\d|2[0-3])\\b)+$|^((\\b(" \
                         "\\d|1\\d|2[0-3])\\b)|\\*)\\/(\\b(\\d|1\\d|2[0-3])\\b)$|^\\*$"
HOURS_RANGE_REGEX_EXPRESSION = "^(\\b(\\d|1\\d|2[0-3])\\b)-(\\b(\\d|1\\d|2[0-3])\\b)$"
DAY_OF_MONTH_REGEX_EXPRESSION = "^\\b(([1-9])|([1-2]\\d)|(3[0-1]))\\b$|^((\\b(([1-9])|([1-2]\\d)|(3[0-1]))\\b)," \
                                ")*(\\b(([1-9])|([1-2]\\d)|(3[0-1]))\\b)+$|^((\\b(([1-9])|([1-2]\\d)|(3[" \
                                "0-1]))\\b)|\\*)\\/(\\b(([1-9])|([1-2]\\d)|(3[0-1]))\\b)$|^\\?$|^\\b(([1-9])|([" \
                                "1-2]\\d)|(3[0-1]))W\\b$|^L$|^\\*$"
DAY_OF_MONTH_RANGE_REGEX_EXPRESSION = "^\\b(([1-9])|([1-2]\\d)|(3[0-1]))\\b-\\b(([1-9])|([1-2]\\d)|(3[0-1]))\\b$"
MONTH_NUMBERS_REGEX_EXPRESSION = "^\\b(\\d|1[0-1])\\b$|^((\\b(\\d|1[0-1])\\b),)*(\\b(\\d|1[0-1])\\b)+$|^\\*$|^(\\b(" \
                                 "\\d|1[0-1])\\b|\\*)\\/(\\b(\\d|1[0-1])\\b)$"
MONTH_ALTERNATIVE_VALUES_REGEX_EXPRESSION = "^(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)$|^((" \
                                            "JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)," \
                                            ")*(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)+$|^\\*$|^((" \
                                            "JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|\\*)\\/(" \
                                            "JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)$"
MONTH_NUMBERS_RANGE_REGEX_EXPRESSION = "^(\\b(\\d|1[0-1])\\b)-(\\b(\\d|1[0-1])\\b)$"
MONTH_ALTERNATIVE_VALUES_RANGE_REGEX_EXPRESSION = "^(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)" \
                                                  "-(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)$"
MONTHS_LIST = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
DAY_OF_WEEK_NUMBERS_REGEX_EXPRESSION = "^[0-6]$|^([0-6],)*[0-6]+$|^[\\*\\?]$|^([0-6]|\\*)\\/[0-6]$|^[0-6]?L$"
DAY_OF_WEEK_NUMBERS_RANGE_REGEX_EXPRESSION = "^[0-6]-[0-6]$"
DAY_OF_WEEK_ALTERNATIVE_VALUES_REGEX_EXPRESSION = "^(SUN|MON|TUE|WED|THU|FRI|SAT)$|^((SUN|MON|TUE|WED|THU|FRI|SAT)," \
                                                  ")*(SUN|MON|TUE|WED|THU|FRI|SAT)+$|^[\\*\\?]$|^((" \
                                                  "SUN|MON|TUE|WED|THU|FRI|SAT)|\\*)\\/(" \
                                                  "SUN|MON|TUE|WED|THU|FRI|SAT)$|^(SUN|MON|TUE|WED|THU|FRI|SAT)?L$"
DAY_OF_WEEK_ALTERNATIVE_VALUES_RANGE_REGEX_EXPRESSION = "^(SUN|MON|TUE|WED|THU|FRI|SAT)-(SUN|MON|TUE|WED|THU|FRI|SAT)$"
DAY_OF_WEEK_LIST = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
YEAR_REGEX_EXPRESSION = "^\\b(197\\d|198\\d|199\\d|20\\d\\d)\\b$|^\\*$|^(\\b(197\\d|198\\d|199\\d|20\\d\\d)\\b," \
                        ")*(\\b(197\\d|198\\d|199\\d|20\\d\\d)\\b)+$|^(\\b(197\\d|198\\d|199\\d|20\\d\\d)\\b|\\*)\\/(" \
                        "\\b(197\\d|198\\d|199\\d|20\\d\\d)\\b)$"
YEAR_RANGE_REGEX_EXPRESSION = "^(\\b(197\\d|198\\d|199\\d|20\\d\\d)\\b)-(\\b(197\\d|198\\d|199\\d|20\\d\\d)\\b)$"


class Validator:

    def validate(self, cron_expression: str) -> bool:
        cron_arguments = cron_expression.rsplit(" ")
        if len(cron_arguments) < 6 or len(cron_arguments) > 7:
            return False
        is_cron_valid = self.validate_seconds_and_minutes(
            cron_arguments[0]) and self.validate_seconds_and_minutes(cron_arguments[1]) and self.validate_hours(
            cron_arguments[2]) and self.validate_day_of_month(cron_arguments[3]) and self.validate_month(
            cron_arguments[4]) and self.validate_day_of_week(cron_arguments[5])
        if len(cron_arguments) == 7:
            return is_cron_valid and self.validate_year(cron_arguments[6])
        return is_cron_valid

    @staticmethod
    def validate_seconds_and_minutes(seconds_and_minutes_expression: str) -> bool:
        range_match = re.findall(SECONDS_AND_MINUTES_RANGE_REGEX_EXPRESSION, seconds_and_minutes_expression)
        if len(range_match) > 0:
            range_values = seconds_and_minutes_expression.rsplit("-")
            return int(range_values[0]) < int(range_values[1])
        return len(re.findall(SECONDS_AND_MINUTES_REGEX_EXPRESSION, seconds_and_minutes_expression)) > 0

    @staticmethod
    def validate_hours(hours_expression: str) -> bool:
        range_match = re.findall(HOURS_RANGE_REGEX_EXPRESSION, hours_expression)
        if len(range_match) > 0:
            range_values = hours_expression.rsplit("-")
            return int(range_values[0]) < int(range_values[1])
        return len(re.findall(HOURS_REGEX_EXPRESSION, hours_expression)) > 0

    @staticmethod
    def validate_day_of_month(day_of_month_expression: str) -> bool:
        range_match = re.findall(DAY_OF_MONTH_RANGE_REGEX_EXPRESSION, day_of_month_expression)
        if len(range_match) > 0:
            range_values = day_of_month_expression.rsplit("-")
            return int(range_values[0]) < int(range_values[1])
        return len(re.findall(DAY_OF_MONTH_REGEX_EXPRESSION, day_of_month_expression)) > 0

    @staticmethod
    def validate_month(month_expression: str) -> bool:
        range_values = []
        if "-" in month_expression:
            range_values = month_expression.rsplit("-")
        if any(alternative_value in month_expression for alternative_value in MONTHS_LIST):
            range_match = re.findall(MONTH_ALTERNATIVE_VALUES_RANGE_REGEX_EXPRESSION, month_expression)
            if len(range_match) > 0:
                return MONTHS_LIST.index(range_values[0]) < MONTHS_LIST.index(range_values[1])
            return len(re.findall(MONTH_ALTERNATIVE_VALUES_REGEX_EXPRESSION, month_expression)) > 0
        range_match = re.findall(MONTH_NUMBERS_RANGE_REGEX_EXPRESSION, month_expression)
        if len(range_match) > 0:
            return int(range_values[0]) < int(range_values[1])
        return len(re.findall(MONTH_NUMBERS_REGEX_EXPRESSION, month_expression)) > 0

    @staticmethod
    def validate_day_of_week(day_of_week_expression: str) -> bool:
        range_values = []
        if "-" in day_of_week_expression:
            range_values = day_of_week_expression.rsplit("-")
        if any(alternative_value in day_of_week_expression for alternative_value in DAY_OF_WEEK_LIST):
            range_match = re.findall(DAY_OF_WEEK_ALTERNATIVE_VALUES_RANGE_REGEX_EXPRESSION, day_of_week_expression)
            if len(range_match) > 0:
                return DAY_OF_WEEK_LIST.index(range_values[0]) < DAY_OF_WEEK_LIST.index(range_values[1])
            return len(re.findall(DAY_OF_WEEK_ALTERNATIVE_VALUES_REGEX_EXPRESSION, day_of_week_expression)) > 0
        range_match = re.findall(DAY_OF_WEEK_NUMBERS_RANGE_REGEX_EXPRESSION, day_of_week_expression)
        if len(range_match) > 0:
            return int(range_values[0]) < int(range_values[1])
        return len(re.findall(DAY_OF_WEEK_NUMBERS_REGEX_EXPRESSION, day_of_week_expression)) > 0

    @staticmethod
    def validate_year(year_expression: str) -> bool:
        range_match = re.findall(YEAR_RANGE_REGEX_EXPRESSION, year_expression)
        if len(range_match) > 0:
            range_values = year_expression.rsplit("-")
            return int(range_values[0]) < int(range_values[1])
        return len(re.findall(YEAR_REGEX_EXPRESSION, year_expression)) > 0
