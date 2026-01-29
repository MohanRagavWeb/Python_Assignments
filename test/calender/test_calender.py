from src.calender.util import get_day_name


def test_known_date_1():
    # 08 05 2015 → WEDNESDAY
    assert get_day_name(8, 5, 2015) == "WEDNESDAY"


def test_known_date_2():
    # 12 25 2020 → FRIDAY
    assert get_day_name(12, 25, 2020) == "FRIDAY"


def test_known_date_3():
    # 01 01 2000 → SATURDAY
    assert get_day_name(1, 1, 2000) == "SATURDAY"


def test_leap_year():
    # 02 29 2020 → SATURDAY
    assert get_day_name(2, 29, 2020) == "SATURDAY"
