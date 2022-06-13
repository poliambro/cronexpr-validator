import unittest
from src.validator import Validator
from src.constants import MONTHS_LIST, DAY_OF_WEEK_LIST


class TestValidator(unittest.TestCase):

    # SECONDS AND MINUTES VALIDATION
    def test_should_validate_every_second_and_minutes_expression(self):
        expression = "*"
        is_valid = Validator.validate_seconds_and_minutes(expression)
        self.assertTrue(is_valid)

    def test_should_validate_step_seconds_and_minutes_expression_when_the_value_is_lesser_than_or_equals_to_59(self):
        star_expression = "*/59"
        number_expression = "0/50"
        is_star_expression_valid = Validator.validate_seconds_and_minutes(star_expression)
        is_number_expression_valid = Validator.validate_seconds_and_minutes(number_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_not_validate_step_seconds_and_minutes_expression_when_the_value_is_greater_than_59(self):
        star_expression = "*/60"
        number_expression = "0/70"
        is_star_expression_valid = Validator.validate_seconds_and_minutes(star_expression)
        is_number_expression_valid = Validator.validate_seconds_and_minutes(number_expression)
        self.assertFalse(is_star_expression_valid)
        self.assertFalse(is_number_expression_valid)

    def test_should_validate_range_seconds_and_minutes_expression_when_first_value_is_lesser_then_the_second_value(
            self):
        range_expression = "5-10"
        is_range_valid = Validator.validate_seconds_and_minutes(range_expression)
        self.assertTrue(is_range_valid)

    def test_should_not_validate_range_seconds_and_minutes_expression_when_first_value_is_greater_than_the_second_value(
            self):
        range_expression = "10-5"
        is_range_valid = Validator.validate_seconds_and_minutes(range_expression)
        self.assertFalse(is_range_valid)

    def test_should_validate_seconds_and_minutes_list_expression_when_values_are_valid(self):
        list_expression = "0,12,15,59"
        is_list_valid = Validator.validate_seconds_and_minutes(list_expression)
        self.assertTrue(is_list_valid)

    def test_should_not_validate_seconds_and_minutes_list_expression_when_values_are_invalid(self):
        list_expression = "0,12,15,60"
        is_list_valid = Validator.validate_seconds_and_minutes(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_not_validate_seconds_and_minutes_list_expression_when_the_list_ends_with_a_comma(self):
        list_expression = "0,12,15,59,"
        is_list_valid = Validator.validate_seconds_and_minutes(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_validate_seconds_and_minutes_range_values_within_list_expression(self):
        list_expression = "0,10,20-30,40-50,59"
        is_list_valid = Validator.validate_seconds_and_minutes(list_expression)
        self.assertTrue(is_list_valid)

    def test_should_not_validate_sec_and_min_range_values_within_list_when_the_first_value_is_greater_than_the_second(
            self):
        list_expression = "0,10,20-30,59-50,59"
        is_list_valid = Validator.validate_seconds_and_minutes(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_not_validate_seconds_and_minutes_range_values_within_list_when_one_of_the_values_is_outside_range(
            self):
        list_expression = "0,10,20-30,40-60,59"
        is_list_valid = Validator.validate_seconds_and_minutes(list_expression)
        self.assertFalse(is_list_valid)

    # HOURS VALIDATION
    def test_should_validate_every_hours_expression(self):
        expression = "*"
        is_valid = Validator.validate_hours(expression)
        self.assertTrue(is_valid)

    def test_should_validate_step_hours_expression_when_the_hour_value_is_lesser_than_or_equals_to_23(self):
        star_expression = "*/23"
        number_expression = "0/12"
        is_star_expression_valid = Validator.validate_hours(star_expression)
        is_number_expression_valid = Validator.validate_hours(number_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_not_validate_step_hours_expression_when_the_hour_value_is_greater_than_23(self):
        star_expression = "*/25"
        number_expression = "0/30"
        is_star_expression_valid = Validator.validate_hours(star_expression)
        is_number_expression_valid = Validator.validate_hours(number_expression)
        self.assertFalse(is_star_expression_valid)
        self.assertFalse(is_number_expression_valid)

    def test_should_validate_range_hours_expression_when_first_value_is_lesser_then_the_second_value(self):
        range_expression = "5-10"
        is_range_valid = Validator.validate_hours(range_expression)
        self.assertTrue(is_range_valid)

    def test_should_not_validate_range_hours_expression_when_first_value_is_greater_than_the_second_value(self):
        range_expression = "15-5"
        is_range_valid = Validator.validate_hours(range_expression)
        self.assertFalse(is_range_valid)

    def test_should_validate_hours_list_expression_when_values_are_valid(self):
        list_expression = "0,12,15,23"
        is_list_valid = Validator.validate_hours(list_expression)
        self.assertTrue(is_list_valid)

    def test_should_not_validate_hours_list_expression_when_values_are_invalid(self):
        list_expression = "0,12,15,24"
        is_list_valid = Validator.validate_hours(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_not_validate_hours_list_expression_when_the_list_ends_with_a_comma(self):
        list_expression = "0,12,15,23,"
        is_list_valid = Validator.validate_hours(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_validate_hours_range_values_within_list_expression(self):
        list_expression = "0,5,10,11-14,19,20-23"
        is_list_valid = Validator.validate_hours(list_expression)
        self.assertTrue(is_list_valid)

    def test_should_not_validate_hours_range_values_within_list_when_the_first_value_is_greater_than_the_second(
            self):
        list_expression = "0,5,10,11-14,19,20-19"
        is_list_valid = Validator.validate_hours(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_not_validate_hours_range_values_within_list_when_one_of_the_values_is_outside_range(self):
        list_expression = "0,10,20-22,22-24,23"
        is_list_valid = Validator.validate_hours(list_expression)
        self.assertFalse(is_list_valid)

    # DAY OF MONTH VALIDATION
    def test_should_validate_every_day_of_month_expression(self):
        star_expression = "*"
        question_mark_expression = "?"
        is_star_valid = Validator.validate_day_of_month(star_expression)
        is_question_mark_valid = Validator.validate_day_of_month(question_mark_expression)
        self.assertTrue(is_star_valid)
        self.assertTrue(is_question_mark_valid)

    def test_should_validate_step_day_of_month_expression_when_the_hour_value_is_lesser_than_or_equals_to_31(self):
        star_expression = "*/31"
        number_expression = "1/31"
        is_star_expression_valid = Validator.validate_day_of_month(star_expression)
        is_number_expression_valid = Validator.validate_day_of_month(number_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_not_validate_step_day_of_month_expression_when_the_hour_value_is_greater_than_31(self):
        star_expression = "*/32"
        number_expression = "2/40"
        is_star_expression_valid = Validator.validate_day_of_month(star_expression)
        is_number_expression_valid = Validator.validate_day_of_month(number_expression)
        self.assertFalse(is_star_expression_valid)
        self.assertFalse(is_number_expression_valid)

    def test_should_validate_range_day_of_month_expression_when_first_value_is_lesser_then_the_second_value(self):
        range_expression = "20-31"
        is_range_valid = Validator.validate_day_of_month(range_expression)
        self.assertTrue(is_range_valid)

    def test_should_not_validate_range_day_of_month_expression_when_first_value_is_greater_than_the_second_value(self):
        range_expression = "15-5"
        is_range_valid = Validator.validate_day_of_month(range_expression)
        self.assertFalse(is_range_valid)

    def test_should_validate_last_day_of_month_expression(self):
        last_day_expression = "L"
        is_last_day_valid = Validator.validate_day_of_month(last_day_expression)
        self.assertTrue(is_last_day_valid)

    def test_should_validate_near_day_of_month_expression(self):
        near_day_3_expression = "3W"
        is_near_day_3_valid = Validator.validate_day_of_month(near_day_3_expression)
        self.assertTrue(is_near_day_3_valid)

    def test_should_not_validate_near_day_without_number_expression(self):
        near_day_without_number_expression = "W"
        is_near_day_without_number_valid = Validator.validate_day_of_month(near_day_without_number_expression)
        self.assertFalse(is_near_day_without_number_valid)

    def test_should_validate_day_of_month_list_expression_when_values_are_valid(self):
        list_expression = "1,12,15,23,31"
        is_list_valid = Validator.validate_day_of_month(list_expression)
        self.assertTrue(is_list_valid)

    def test_should_not_validate_day_of_month_list_expression_when_values_are_invalid(self):
        list_expression = "0,12,15,24"
        is_list_valid = Validator.validate_day_of_month(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_not_validate_day_of_month_list_expression_when_the_list_ends_with_a_comma(self):
        list_expression = "1,12,15,23,"
        is_list_valid = Validator.validate_day_of_month(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_validate_day_of_month_range_values_within_list_expression(self):
        list_expression = "1,5,10,11-14,19,20-23"
        is_list_valid = Validator.validate_day_of_month(list_expression)
        self.assertTrue(is_list_valid)

    def test_should_not_validate_day_of_month_range_values_within_list_when_the_first_value_is_greater_than_the_second(
            self):
        list_expression = "1,5,10,11-14,19,20-19"
        is_list_valid = Validator.validate_day_of_month(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_not_validate_day_of_month_range_values_within_list_when_one_of_the_values_is_outside_range(self):
        list_expression = "1,10,20-22,22-32,23"
        is_list_valid = Validator.validate_day_of_month(list_expression)
        self.assertFalse(is_list_valid)

    # MONTH VALIDATIONS
    def test_should_validate_every_month_expression(self):
        expression = "*"
        is_valid = Validator.validate_month(expression)
        self.assertTrue(is_valid)

    def test_should_validate_step_month_expression_when_the_month_value_is_lesser_than_or_equals_to_12(self):
        star_expression = "*/12"
        number_expression = "1/12"
        is_star_expression_valid = Validator.validate_month(star_expression)
        is_number_expression_valid = Validator.validate_month(number_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_not_validate_step_month_expression_when_the_month_value_is_greater_than_12(self):
        star_expression = "*/13"
        number_expression = "1/14"
        is_star_expression_valid = Validator.validate_month(star_expression)
        is_number_expression_valid = Validator.validate_month(number_expression)
        self.assertFalse(is_star_expression_valid)
        self.assertFalse(is_number_expression_valid)

    def test_should_validate_range_month_expression_when_first_value_is_lesser_then_the_second_value(self):
        range_expression = "5-10"
        is_range_valid = Validator.validate_month(range_expression)
        self.assertTrue(is_range_valid)

    def test_should_not_validate_range_month_expression_when_first_value_is_greater_than_the_second_value(self):
        range_expression = "11-5"
        is_range_valid = Validator.validate_month(range_expression)
        self.assertFalse(is_range_valid)

    def test_should_validate_month_expression_with_alternative_single_values(self):
        for month in MONTHS_LIST:
            is_month_valid = Validator.validate_month(month)
            if not is_month_valid:
                self.fail(f"Test failed for month {month}. Check your regex expression.")

    def test_should_accept_month_alternative_single_values_for_range_expression(self):
        range_expression = "JAN-JUL"
        is_range_valid = Validator.validate_month(range_expression)
        self.assertTrue(is_range_valid)

    def test_should_not_validate_range_expression_when_the_first_month_is_before_the_second_month_in_calendar(self):
        range_expression = "JUL-FEB"
        is_range_valid = Validator.validate_month(range_expression)
        self.assertFalse(is_range_valid)

    def test_should_validate_step_month_expression_with_alternative_values(self):
        star_expression = "*/DEC"
        alternative_expression = "MAR/JAN"
        is_star_expression_valid = Validator.validate_month(star_expression)
        is_number_expression_valid = Validator.validate_month(alternative_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_validate_month_list_expression_when_values_are_valid(self):
        numbers_list_expression = "1,3,4"
        alternative_list_expression = "JAN,MAR,APR"
        is_numbers_list_valid = Validator.validate_month(numbers_list_expression)
        is_alternative_list_valid = Validator.validate_month(alternative_list_expression)
        self.assertTrue(is_numbers_list_valid)
        self.assertTrue(is_alternative_list_valid)

    def test_should_not_validate_month_list_expression_when_values_are_invalid(self):
        numbers_list_expression = "1,3,4,13"
        alternative_list_expression = "JAN,MAR,APR,JUH"
        is_numbers_list_valid = Validator.validate_month(numbers_list_expression)
        is_alternative_list_valid = Validator.validate_month(alternative_list_expression)
        self.assertFalse(is_numbers_list_valid)
        self.assertFalse(is_alternative_list_valid)

    def test_should_not_validate_month_list_expression_when_the_list_ends_with_a_comma(self):
        numbers_list_expression = "1,3,4,12,"
        alternative_list_expression = "JAN,MAR,APR,JUN,"
        is_numbers_list_valid = Validator.validate_month(numbers_list_expression)
        is_alternative_list_valid = Validator.validate_month(alternative_list_expression)
        self.assertFalse(is_numbers_list_valid)
        self.assertFalse(is_alternative_list_valid)

    def test_should_validate_month_range_values_within_list_expression(self):
        list_expression = "1,5-7,8,10-12"
        alternative_list_expression = "JAN,FEB,MAR-JUL,SEP-DEC"
        is_list_valid = Validator.validate_month(list_expression)
        is_alternative_list_valid = Validator.validate_month(alternative_list_expression)
        self.assertTrue(is_list_valid)
        self.assertTrue(is_alternative_list_valid)

    def test_should_not_validate_month_range_values_within_list_when_the_first_value_is_greater_than_the_second(
            self):
        list_expression = "1,8-7,8,10-11"
        alternative_list_expression = "JAN,FEB,DEC-JUL,SEP-DEC"
        is_list_valid = Validator.validate_month(list_expression)
        is_alternative_list_valid = Validator.validate_month(alternative_list_expression)
        self.assertFalse(is_list_valid)
        self.assertFalse(is_alternative_list_valid)

    def test_should_not_validate_month_range_values_within_list_when_one_of_the_values_is_outside_range(self):
        list_expression = "1,5-7,8,10-14"
        alternative_list_expression = "JAN,FEB,MAR-JUL,SEP-TES"
        is_list_valid = Validator.validate_month(list_expression)
        is_alternative_list_valid = Validator.validate_month(alternative_list_expression)
        self.assertFalse(is_list_valid)
        self.assertFalse(is_alternative_list_valid)

    # DAY OF THE WEEK VALIDATIONS
    def test_should_validate_every_day_of_week_expression(self):
        star_expression = "*"
        question_mark_expression = "?"
        is_star_expression_valid = Validator.validate_day_of_week(star_expression)
        is_question_mark_expression_valid = Validator.validate_day_of_week(question_mark_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_question_mark_expression_valid)

    def test_should_validate_step_day_of_week_expression_when_the_day_of_week_value_is_lesser_than_or_equals_to_6(self):
        star_expression = "*/6"
        number_expression = "0/6"
        is_star_expression_valid = Validator.validate_day_of_week(star_expression)
        is_number_expression_valid = Validator.validate_day_of_week(number_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_not_validate_step_day_of_week_expression_when_the_day_of_week_value_is_greater_than_6(self):
        star_expression = "*/7"
        number_expression = "0/7"
        is_star_expression_valid = Validator.validate_day_of_week(star_expression)
        is_number_expression_valid = Validator.validate_day_of_week(number_expression)
        self.assertFalse(is_star_expression_valid)
        self.assertFalse(is_number_expression_valid)

    def test_should_validate_range_day_of_week_expression_when_first_value_is_lesser_then_the_second_value(self):
        range_expression = "1-3"
        is_range_valid = Validator.validate_day_of_week(range_expression)
        self.assertTrue(is_range_valid)

    def test_should_not_validate_range_day_of_week_expression_when_first_value_is_greater_than_the_second_value(self):
        range_expression = "6-2"
        is_range_valid = Validator.validate_day_of_week(range_expression)
        self.assertFalse(is_range_valid)

    def test_should_validate_day_of_week_expression_with_alternative_single_values(self):
        for day_of_week in DAY_OF_WEEK_LIST:
            is_day_of_week_valid = Validator.validate_day_of_week(day_of_week)
            if not is_day_of_week_valid:
                self.fail(f"Test failed for day of week: {day_of_week}. Check your regex expression.")

    def test_should_accept_day_of_week_alternative_single_values_for_range_expression(self):
        range_expression = "SUN-TUE"
        is_range_valid = Validator.validate_day_of_week(range_expression)
        self.assertTrue(is_range_valid)

    def test_should_not_validate_range_expression_when_the_first_day_of_week_is_before_the_second_day_of_week(self):
        range_expression = "FRI-MON"
        is_range_valid = Validator.validate_day_of_week(range_expression)
        self.assertFalse(is_range_valid)

    def test_should_validate_last_day_of_week_expression(self):
        last_day_expression = "L"
        last_day_expression_with_number_day = "3L"
        last_day_expression_with_alternative_value_day = "MONL"
        is_last_day_valid = Validator.validate_day_of_week(last_day_expression)
        is_last_day_expression_with_number_day_valid = \
            Validator.validate_day_of_week(last_day_expression_with_number_day)
        is_last_day_expression_with_alternative_value_day_valid = \
            Validator.validate_day_of_week(last_day_expression_with_alternative_value_day)
        self.assertTrue(is_last_day_valid)
        self.assertTrue(is_last_day_expression_with_number_day_valid)
        self.assertTrue(is_last_day_expression_with_alternative_value_day_valid)

    def test_should_validate_step_day_of_week_expression_when_the_day_of_week_value_is_alternative(self):
        star_expression = "*/FRI"
        number_expression = "MON/WED"
        is_star_expression_valid = Validator.validate_day_of_week(star_expression)
        is_number_expression_valid = Validator.validate_day_of_week(number_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_validate_day_of_week_list_expression_when_values_are_valid(self):
        numbers_list_expression = "1,3,4"
        alternative_list_expression = "SUN,TUE,THU"
        is_numbers_list_valid = Validator.validate_day_of_week(numbers_list_expression)
        is_alternative_list_valid = Validator.validate_day_of_week(alternative_list_expression)
        self.assertTrue(is_numbers_list_valid)
        self.assertTrue(is_alternative_list_valid)

    def test_should_not_validate_day_of_week_list_expression_when_values_are_invalid(self):
        numbers_list_expression = "1,3,4,7"
        alternative_list_expression = "SUN,TUE,THU,FRE"
        is_numbers_list_valid = Validator.validate_day_of_week(numbers_list_expression)
        is_alternative_list_valid = Validator.validate_day_of_week(alternative_list_expression)
        self.assertFalse(is_numbers_list_valid)
        self.assertFalse(is_alternative_list_valid)

    def test_should_not_validate_day_of_week_list_expression_when_the_list_ends_with_a_comma(self):
        numbers_list_expression = "1,3,4,"
        alternative_list_expression = "SUN,TUE,THU,"
        is_numbers_list_valid = Validator.validate_day_of_week(numbers_list_expression)
        is_alternative_list_valid = Validator.validate_day_of_week(alternative_list_expression)
        self.assertFalse(is_numbers_list_valid)
        self.assertFalse(is_alternative_list_valid)
        
    def test_should_validate_day_of_week_range_values_within_list_expression(self):
        list_expression = "0,2,3-5,6"
        alternative_list_expression = "SUN,MON,WED-FRI,SAT"
        is_list_valid = Validator.validate_day_of_week(list_expression)
        is_alternative_list_valid = Validator.validate_day_of_week(alternative_list_expression)
        self.assertTrue(is_list_valid)
        self.assertTrue(is_alternative_list_valid)

    def test_should_not_validate_day_of_week_range_values_within_list_when_the_first_value_is_greater_than_the_second(
            self):
        list_expression = "0,3-5,6-2"
        alternative_list_expression = "SUN,THU-MON,SAT"
        is_list_valid = Validator.validate_day_of_week(list_expression)
        is_alternative_list_valid = Validator.validate_day_of_week(alternative_list_expression)
        self.assertFalse(is_list_valid)
        self.assertFalse(is_alternative_list_valid)

    def test_should_not_validate_day_of_week_range_values_within_list_when_one_of_the_values_is_outside_range(self):
        list_expression = "0,2-5,6,8"
        alternative_list_expression = "SUN,MON,THU-FRI,TES"
        is_list_valid = Validator.validate_day_of_week(list_expression)
        is_alternative_list_valid = Validator.validate_day_of_week(alternative_list_expression)
        self.assertFalse(is_list_valid)
        self.assertFalse(is_alternative_list_valid)

    # YEAR VALIDATION
    def test_should_validate_every_year_expression(self):
        star_expression = "*"
        is_star_expression_valid = Validator.validate_year(star_expression)
        self.assertTrue(is_star_expression_valid)

    def test_should_validate_step_year_expression_when_the_year_value_is_lesser_than_or_equals_to_2099(self):
        star_expression = "*/2099"
        number_expression = "1970/2023"
        is_star_expression_valid = Validator.validate_year(star_expression)
        is_number_expression_valid = Validator.validate_year(number_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_validate_step_year_expression_when_the_year_value_is_greater_than_or_equals_to_1970(self):
        star_expression = "*/1970"
        number_expression = "1970/1985"
        is_star_expression_valid = Validator.validate_year(star_expression)
        is_number_expression_valid = Validator.validate_year(number_expression)
        self.assertTrue(is_star_expression_valid)
        self.assertTrue(is_number_expression_valid)

    def test_should_not_validate_step_year_expression_when_the_year_value_is_greater_than_2099(self):
        star_expression = "*/3000"
        number_expression = "1975/3050"
        is_star_expression_valid = Validator.validate_year(star_expression)
        is_number_expression_valid = Validator.validate_year(number_expression)
        self.assertFalse(is_star_expression_valid)
        self.assertFalse(is_number_expression_valid)

    def test_should_not_validate_step_year_expression_when_the_year_value_is_lesser_than_1970(self):
        star_expression = "*/1969"
        number_expression = "1930/1975"
        is_star_expression_valid = Validator.validate_year(star_expression)
        is_number_expression_valid = Validator.validate_year(number_expression)
        self.assertFalse(is_star_expression_valid)
        self.assertFalse(is_number_expression_valid)

    def test_should_validate_range_year_expression_when_first_value_is_lesser_then_the_second_value(self):
        range_expression = "1970-2023"
        is_range_valid = Validator.validate_year(range_expression)
        self.assertTrue(is_range_valid)

    def test_should_not_validate_range_year_expression_when_first_value_is_greater_than_the_second_value(self):
        range_expression = "2030-2001"
        is_range_valid = Validator.validate_year(range_expression)
        self.assertFalse(is_range_valid)

    def test_should_validate_year_range_values_within_list_expression(self):
        list_expression = "1970,1975-1985,1990,2000-2010"
        is_list_valid = Validator.validate_year(list_expression)
        self.assertTrue(is_list_valid)

    def test_should_not_validate_year_range_values_within_list_when_the_first_value_is_greater_than_the_second(
            self):
        list_expression = "1970,2000-1990,2022,2099"
        is_list_valid = Validator.validate_year(list_expression)
        self.assertFalse(is_list_valid)

    def test_should_not_validate_year_range_values_within_list_when_one_of_the_values_is_outside_range(self):
        list_expression = "1980,1990,2000,2009,2010-3000"
        is_list_valid = Validator.validate_year(list_expression)
        self.assertFalse(is_list_valid)

    # VALIDATIONS WITH FULL CRON EXPRESSIONS
    def test_should_validate_six_positional_arguments_expression(self):
        validator = Validator()
        six_cron_expression = "0 0 12 * * *"
        is_cron_valid = validator.validate(six_cron_expression)
        self.assertTrue(is_cron_valid)

    def test_should_validate_seven_positional_arguments_expression(self):
        seven_cron_expression = "0 0/5 14,18,23 ? JAN,MAR,SEP MON-FRI 2002-2010"
        is_cron_valid = Validator.validate(seven_cron_expression)
        self.assertTrue(is_cron_valid)

    def test_should_not_validate_expressions_with_less_than_six_positional_arguments(self):
        five_cron_expression = "* * * * *"
        is_cron_valid = Validator.validate(five_cron_expression)
        self.assertFalse(is_cron_valid)

    def test_should_not_validate_expressions_with_more_than_seven_positional_arguments(self):
        eight_cron_expression = "* * * * * * * *"
        is_cron_valid = Validator.validate(eight_cron_expression)
        self.assertFalse(is_cron_valid)
