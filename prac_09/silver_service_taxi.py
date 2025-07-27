"""
CP1404/CP5632 Practical
silver_service_taxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A fancy version of Taxi with additional charges."""

    flagfall = 4.50  # Class variable for the additional charge per fare

    def __init__(self, name, fuel, fanciness):
        """
        Initialize a SilverServiceTaxi instance.

        Args:
            name (str): Name of the taxi
            fuel (float): Starting fuel amount
            fanciness (float): Multiplier for base price_per_km
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness  # Scale the base price by fanciness

    def get_fare(self):
        """Calculate the total fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation with flagfall information."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"