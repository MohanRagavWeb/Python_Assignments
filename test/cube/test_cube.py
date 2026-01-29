from src.cube.util import can_stack_blocks


def test_possible_case():
    blocks = [4, 3, 2, 1, 3, 4]
    assert can_stack_blocks(blocks) is True


def test_impossible_case():
    blocks = [1, 3, 2]
    assert can_stack_blocks(blocks) is False


def test_single_block():
    blocks = [10]
    assert can_stack_blocks(blocks) is True


def test_already_sorted():
    blocks = [5, 4, 3, 2, 1]
    assert can_stack_blocks(blocks) is True


def test_equal_blocks():
    blocks = [3, 3, 3, 3]
    assert can_stack_blocks(blocks) is True
