from src.wordorder.util import count_words


def test_basic_case():
    words = ["bcdef", "abcdefg", "bcde", "bcdef"]
    unique_count, counts = count_words(words)

    assert unique_count == 3
    assert counts == [2, 1, 1]


def test_all_unique():
    words = ["one", "two", "three"]
    unique_count, counts = count_words(words)

    assert unique_count == 3
    assert counts == [1, 1, 1]


def test_all_same():
    words = ["hello", "hello", "hello"]
    unique_count, counts = count_words(words)

    assert unique_count == 1
    assert counts == [3]


def test_mixed_case():
    words = ["a", "b", "a", "c", "b", "a"]
    unique_count, counts = count_words(words)

    assert unique_count == 3
    assert counts == [3, 2, 1]


def test_single_word():
    words = ["python"]
    unique_count, counts = count_words(words)

    assert unique_count == 1
    assert counts == [1]
