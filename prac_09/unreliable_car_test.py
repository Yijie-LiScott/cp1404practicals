from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    # Create an unreliable car with 50% reliability
    unreliable_car = UnreliableCar("Old Clunker", 100, 50.0)

    # Test driving multiple times
    successful_drives = 0
    test_runs = 100

    print(f"Testing {unreliable_car.name} with {unreliable_car.reliability}% reliability")

    for i in range(test_runs):
        distance_driven = unreliable_car.drive(10)
        if distance_driven > 0:
            successful_drives += 1

    print(f"Attempted to drive {test_runs} times")
    print(f"Successfully drove {successful_drives} times")
    print(f"Expected success rate: {unreliable_car.reliability}%")
    print(f"Actual success rate: {(successful_drives / test_runs) * 100:.1f}%")
    print(f"Final odometer: {unreliable_car.odometer}")
    print(f"Final fuel: {unreliable_car.fuel}")


if __name__ == '__main__':
    main()