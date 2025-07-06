"""
Guitar Class
Estimate: 25 minutes
Actual:   21 minutes
"""

CURRENT_YEAR = 2025  # Set current year here for get_age() and is_vintage()

class Guitar:
    """Represents a Guitar with name, year, and cost attributes."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string like: Gibson L-5 CES (1922) : $16,035.40"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 or more years old)."""
        return self.get_age() >= 50
