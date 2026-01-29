import pytest
from src.textalign.util import text_aligning


def test_sample_input_5():
    expected_start = [
        "    H    ",
        "   HHH   ",
        "  HHHHH  ",
        " HHHHHHH ",
        "HHHHHHHHH"
    ]
    result = text_aligning(5)
    assert result[0:5] == expected_start


def test_invalid_even_thickness():
    with pytest.raises(ValueError):
        text_aligning(4)
