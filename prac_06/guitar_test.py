"""
Guitar Test
Estimate: 18 minutes
Actual:   15 minutes
"""

from guitar import Guitar

CURRENT_YEAR = 2025  # Must match the year used in guitar.py

def main():
    """Test get_age() and is_vintage() methods of the Guitar class."""
    # Test guitars
    test_guitar_1 = Guitar("Gibson L-5 CES", 1925, 16035.40)
    test_guitar_2 = Guitar("Another Guitar", 2016, 1500)

    # Expected results
    expected_age_1 = CURRENT_YEAR - 1925  # 100
    expected_age_2 = CURRENT_YEAR - 2016  # 9
    expected_vintage_1 = True
    expected_vintage_2 = False

    # Test get_age()
    print(f"{test_guitar_1.name} get_age() - Expected {expected_age_1}. Got {test_guitar_1.get_age()}")
    print(f"{test_guitar_2.name} get_age() - Expected {expected_age_2}. Got {test_guitar_2.get_age()}")

    # Test is_vintage()
    print(f"{test_guitar_1.name} is_vintage() - Expected {expected_vintage_1}. Got {test_guitar_1.is_vintage()}")
    print(f"{test_guitar_2.name} is_vintage() - Expected {expected_vintage_2}. Got {test_guitar_2.is_vintage()}")


if __name__ == "__main__":
    main()
