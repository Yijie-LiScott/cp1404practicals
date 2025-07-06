"""
Programming Language Class
Estimate: 20 minutes
Actual:   17 minutes
"""


class ProgrammingLanguage:
    """Represents a programming language with typing, reflection and year info."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return string representation like: Python, Dynamic Typing, Reflection=True, First appeared in 1991"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
