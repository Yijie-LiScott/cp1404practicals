"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)  # Fixed by using join to add spaces between repeats


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length  # Fixed by changing > to >= to match test cases


def format_sentence(phrase):
    """
    Format a phrase as a sentence starting with capital and ending with single full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this needs formatting')
    'This needs formatting.'
    """
    # Remove any existing trailing punctuation
    phrase = phrase.rstrip('.!?')
    # Capitalize first letter and add full stop
    return phrase[0].upper() + phrase[1:] + '.'


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass after fixing repeat_string
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test Car sets fuel correctly with default value
    car = Car()
    assert car.fuel == 0, "Car does not set default fuel correctly"

    # Test Car sets fuel correctly with value passed in
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set passed fuel value correctly"


run_tests()

# Uncomment to run doctests
doctest.testmod()