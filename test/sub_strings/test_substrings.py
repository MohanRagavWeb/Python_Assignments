from src.sub_strings.util import merge_the_tools


def test_basic_case():
    assert merge_the_tools("AABCAAADA", 3) == ["AB", "CA", "AD"]


def test_all_unique():
    assert merge_the_tools("ABCDEFGH", 2) == ["AB", "CD", "EF", "GH"]


def test_all_duplicates():
    assert merge_the_tools("AAAAAA", 2) == ["A", "A", "A"]


def test_mixed_case():
    assert merge_the_tools("BANANA", 3) == ["BAN", "AN"]


def test_single_char_chunks():
    assert merge_the_tools("PYTHON", 1) == ["P", "Y", "T", "H", "O", "N"]
