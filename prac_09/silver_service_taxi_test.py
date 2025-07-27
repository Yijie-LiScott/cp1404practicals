"""
CP1404/CP5632 Practical
silver_service_taxi_test
"""
from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    """Test the SilverServiceTaxi class."""
    # Test initialization
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)
    assert fancy_taxi.name == "Hummer"
    assert fancy_taxi.fuel == 200
    assert fancy_taxi.fanciness == 4
    assert fancy_taxi.price_per_km == Taxi.price_per_km * 4

    # Test fare calculation with flagfall
    fancy_taxi.start_fare()
    fancy_taxi.drive(10)
    expected_fare = (10 * fancy_taxi.price_per_km) + fancy_taxi.flagfall
    assert abs(fancy_taxi.get_fare() - expected_fare) < 0.01

    # Test specific example from requirements
    test_taxi = SilverServiceTaxi("Test", 100, 2)
    test_taxi.start_fare()
    test_taxi.drive(18)
    assert abs(test_taxi.get_fare() - 48.78) < 0.01, "Fare calculation incorrect for 18km trip with fanciness 2"

    print("All tests passed!")


if __name__ == '__main__':
    test_silver_service_taxi()