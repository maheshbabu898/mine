"""
If you pass a string to reversed(), 
you get an iterator that yields characters in reverse order:
"""


def is_palindrome(text):
    reverse = str.join(" ", reversed(text))
    return text == reverse
