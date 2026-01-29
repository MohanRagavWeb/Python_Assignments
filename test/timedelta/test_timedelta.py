from src.timedelta.util import time_delta


def test_basic_case():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"
    assert time_delta(t1, t2) == "25200"


def test_same_time():
    t1 = "Sat 02 May 2015 19:54:36 +0530"
    t2 = "Sat 02 May 2015 19:54:36 +0530"
    assert time_delta(t1, t2) == "0"


def test_reverse_order():
    t1 = "Fri 11 Feb 2022 10:00:00 +0000"
    t2 = "Fri 11 Feb 2022 09:00:00 +0000"
    assert time_delta(t1, t2) == "3600"


def test_different_zones():
    t1 = "Mon 01 Jan 2024 12:00:00 +0530"
    t2 = "Mon 01 Jan 2024 12:00:00 +0000"
    assert time_delta(t1, t2) == "19800"
