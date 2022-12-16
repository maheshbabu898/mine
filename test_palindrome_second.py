"""
def test_is_palindrome_<in some situation>():
    assert is_palindrome("<some string>")
"""
import pytest
import palindrome_checker


@pytest.mark.parametrize(
    "palindrome",
    [
        "",
        "a",
        "Bob",
        "Never odd or even",
        "Do geese see God?",
    ],
)
def test_is_palindrome(palindrome):
    assert palindrome_checker.is_palindrome(palindrome)


@pytest.mark.parametrize(
    "non_palindrome",
    [
        "abc",
        "abab",
    ],
)
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not palindrome_checker.is_palindrome(non_palindrome)
