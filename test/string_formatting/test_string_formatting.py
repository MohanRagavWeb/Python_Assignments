from src.string_formatting.util import format_numbers


def test_small_number():
    assert format_numbers(2) == [
        " 1  1  1  1",
        " 2  2  2 10"
    ]



def test_medium_number():
    assert format_numbers(5) == [
        "  1   1   1   1",
        "  2   2   2  10",
        "  3   3   3  11",
        "  4   4   4 100",
        "  5   5   5 101"
    ]


def test_single_value():
    assert format_numbers(1) == ["1 1 1 1"]


def test_width_alignment():
    output = format_numbers(8)
    assert output[-1].endswith("1000")
