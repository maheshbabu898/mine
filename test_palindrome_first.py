import palindrome_checker


def test_is_palindrome_empty_string():
    assert palindrome_checker.is_palindrome("")


def test_is_palindrome_single_character():
    assert palindrome_checker.is_palindrome("a")


def test_is_palindrome_mixed_casing():
    assert palindrome_checker.is_palindrome("Bob")


def test_is_palindrome_with_spaces():
    assert palindrome_checker.is_palindrome("Never odd or even")


def test_is_palindrome_with_punctuation():
    assert palindrome_checker.is_palindrome("Do geese see God?")


def test_is_palindrome_not_palindrome():
    assert not palindrome_checker.is_palindrome("abc")


def test_is_palindrome_not_quite():
    assert not palindrome_checker.is_palindrome("abab")
