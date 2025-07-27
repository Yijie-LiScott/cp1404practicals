"""
CP1404/CP5632 Practical
unreliable_car
"""


import random
from car import Car


class UnreliableCar(Car):
    """A version of Car that doesn't always drive when asked."""

    def __init__(self, name, fuel, reliability):
        """
        Initialize an UnreliableCar instance.

        Args:
            name (str): Name of the car
            fuel (float): Starting fuel amount
            reliability (float): Percentage chance (0-100) that drive() will work
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Attempt to drive the car, but only works based on reliability.

        Args:
            distance (float): Distance to attempt to drive

        Returns:
            float: Distance actually driven (0 if car didn't start)
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0

    def __str__(self):
        """Return string representation of UnreliableCar."""
        return f"{super().__str__()}, {self.reliability}% reliable"