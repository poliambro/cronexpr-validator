import re
from src import constants


class Validator:

    def validate(self, cron_expression: str) -> bool:
        """
            Validates a given cron expression and returns a boolean evaluated value.

            Fields -------- Required -------- Allowed values -------- Allowed Special Characters
            Seconds            Y              0-59                    ,-*/
            Minutes            Y              0-59                    ,-*/
            Hours              Y              0-23                    ,-*/
            Day of Month       Y              1-31                    ,-*/? L W
            Month              Y              0-11 or JAN-DEC         ,-*/
            Day of Week        Y              0-6 or SUN-SAT          ,-*/? L
            Year               N              empty or 1970-2099      ,-*/
        """
        # TODO: Add range validations inside lists
        cron_arguments = cron_expression.rsplit(" ")
        if len(cron_arguments) < constants.CRON_EXPRESSION_MIN_ARGUMENTS or \
                len(cron_arguments) > constants.CRON_EXPRESSION_MAX_ARGUMENTS:
            return False
        is_cron_valid = self.validate_seconds_and_minutes(
            cron_arguments[constants.SECONDS_SUBEXPRESSION_INDEX]) and self.validate_seconds_and_minutes(
            cron_arguments[constants.MINUTES_SUBEXPRESSION_INDEX]) and self.validate_hours(
            cron_arguments[constants.HOURS_SUBEXPRESSION_INDEX]) and self.validate_day_of_month(
            cron_arguments[constants.DAY_OF_MONTH_SUBEXPRESSION_INDEX]) and self.validate_month(
            cron_arguments[constants.MONTH_SUBEXPRESSION_INDEX]) and self.validate_day_of_week(
            cron_arguments[constants.DAY_OF_WEEK_SUBEXPRESSION_INDEX])
        if len(cron_arguments) == constants.CRON_EXPRESSION_MAX_ARGUMENTS:
            return is_cron_valid and self.validate_year(cron_arguments[constants.YEAR_SUBEXPRESSION_INDEX])
        return is_cron_valid

    @staticmethod
    def validate_seconds_and_minutes(seconds_and_minutes_expression: str) -> bool:
        """
            Validates a cron subexpression of seconds or minutes and returns a boolean evaluated value.
        """
        range_match = re.findall(constants.SECONDS_AND_MINUTES_RANGE_REGEX_EXPRESSION, seconds_and_minutes_expression)
        if len(range_match) > 0:
            range_values = seconds_and_minutes_expression.rsplit(constants.RANGE_ELEMENT_DELIMITER)
            return int(range_values[constants.FIRST_RANGE_ELEMENT_INDEX]) < \
                   int(range_values[constants.SECOND_RANGE_ELEMENT_INDEX])
        return len(re.findall(constants.SECONDS_AND_MINUTES_REGEX_EXPRESSION, seconds_and_minutes_expression)) > 0

    @staticmethod
    def validate_hours(hours_expression: str) -> bool:
        """
            Validates a cron subexpression of hours and returns a boolean evaluated value.
        """
        range_match = re.findall(constants.HOURS_RANGE_REGEX_EXPRESSION, hours_expression)
        if len(range_match) > 0:
            range_values = hours_expression.rsplit(constants.RANGE_ELEMENT_DELIMITER)
            return int(range_values[constants.FIRST_RANGE_ELEMENT_INDEX]) < \
                   int(range_values[constants.SECOND_RANGE_ELEMENT_INDEX])
        return len(re.findall(constants.HOURS_REGEX_EXPRESSION, hours_expression)) > 0

    @staticmethod
    def validate_day_of_month(day_of_month_expression: str) -> bool:
        """
            Validates a cron subexpression of the day of the month and returns a boolean evaluated value.
        """
        range_match = re.findall(constants.DAY_OF_MONTH_RANGE_REGEX_EXPRESSION, day_of_month_expression)
        if len(range_match) > 0:
            range_values = day_of_month_expression.rsplit(constants.RANGE_ELEMENT_DELIMITER)
            return int(range_values[constants.FIRST_RANGE_ELEMENT_INDEX]) < \
                   int(range_values[constants.SECOND_RANGE_ELEMENT_INDEX])
        return len(re.findall(constants.DAY_OF_MONTH_REGEX_EXPRESSION, day_of_month_expression)) > 0

    @staticmethod
    def validate_month(month_expression: str) -> bool:
        """
            Validates a cron subexpression of the month and returns a boolean evaluated value.
        """
        range_values = []
        if "-" in month_expression:
            range_values = month_expression.rsplit(constants.RANGE_ELEMENT_DELIMITER)
        if any(alternative_value in month_expression for alternative_value in constants.MONTHS_LIST):
            range_match = re.findall(constants.MONTH_ALTERNATIVE_VALUES_RANGE_REGEX_EXPRESSION, month_expression)
            if len(range_match) > 0:
                return constants.MONTHS_LIST.index(range_values[constants.FIRST_RANGE_ELEMENT_INDEX]) < \
                       constants.MONTHS_LIST.index(range_values[constants.SECOND_RANGE_ELEMENT_INDEX])
            return len(re.findall(constants.MONTH_ALTERNATIVE_VALUES_REGEX_EXPRESSION, month_expression)) > 0
        range_match = re.findall(constants.MONTH_NUMBERS_RANGE_REGEX_EXPRESSION, month_expression)
        if len(range_match) > 0:
            return int(range_values[constants.FIRST_RANGE_ELEMENT_INDEX]) < \
                   int(range_values[constants.SECOND_RANGE_ELEMENT_INDEX])
        return len(re.findall(constants.MONTH_NUMBERS_REGEX_EXPRESSION, month_expression)) > 0

    @staticmethod
    def validate_day_of_week(day_of_week_expression: str) -> bool:
        """
            Validates a cron subexpression of the day of the week and returns a boolean evaluated value.
        """
        range_values = []
        if "-" in day_of_week_expression:
            range_values = day_of_week_expression.rsplit(constants.RANGE_ELEMENT_DELIMITER)
        if any(alternative_value in day_of_week_expression for alternative_value in constants.DAY_OF_WEEK_LIST):
            range_match = re.findall(
                constants.DAY_OF_WEEK_ALTERNATIVE_VALUES_RANGE_REGEX_EXPRESSION, day_of_week_expression)
            if len(range_match) > 0:
                return constants.DAY_OF_WEEK_LIST.index(range_values[constants.FIRST_RANGE_ELEMENT_INDEX]) < \
                       constants.DAY_OF_WEEK_LIST.index(range_values[constants.SECOND_RANGE_ELEMENT_INDEX])
            return len(re.findall(
                constants.DAY_OF_WEEK_ALTERNATIVE_VALUES_REGEX_EXPRESSION, day_of_week_expression)) > 0
        range_match = re.findall(constants.DAY_OF_WEEK_NUMBERS_RANGE_REGEX_EXPRESSION, day_of_week_expression)
        if len(range_match) > 0:
            return int(range_values[constants.FIRST_RANGE_ELEMENT_INDEX]) < \
                   int(range_values[constants.SECOND_RANGE_ELEMENT_INDEX])
        return len(re.findall(constants.DAY_OF_WEEK_NUMBERS_REGEX_EXPRESSION, day_of_week_expression)) > 0

    @staticmethod
    def validate_year(year_expression: str) -> bool:
        """
            Validates a cron subexpression of the year and returns a boolean evaluated value.
        """
        range_match = re.findall(constants.YEAR_RANGE_REGEX_EXPRESSION, year_expression)
        if len(range_match) > 0:
            range_values = year_expression.rsplit(constants.RANGE_ELEMENT_DELIMITER)
            return int(range_values[constants.FIRST_RANGE_ELEMENT_INDEX]) < \
                   int(range_values[constants.SECOND_RANGE_ELEMENT_INDEX])
        return len(re.findall(constants.YEAR_REGEX_EXPRESSION, year_expression)) > 0
