from src.email.util import filter_mail, is_valid_email


def test_valid_email():
    assert is_valid_email("test_user-1@gmail.com") is True


def test_invalid_email_missing_at():
    assert is_valid_email("testgmail.com") is False


def test_invalid_domain():
    assert is_valid_email("user@domain.toolong") is False


def test_filter_emails():
    emails = [
        "lara@hackerrank.com",
        "invalid-email",
        "abc_123@gmail.com",
        "wrong@domain.corporate"
    ]
    assert filter_mail(emails) == [
        "abc_123@gmail.com",
        "lara@hackerrank.com"
    ]


def test_empty_list():
    assert filter_mail([]) == []
