"""
CP1404/CP5632 Practical
taxi_simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_menu():
    """Display the main menu options."""
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis(taxis):
    """Display available taxis with their indexes."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def main():
    """Main taxi simulator program."""
    # Create a list of available taxis
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limosine", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill_to_date = 0.00

    print("Let's drive!")

    while True:
        print(f"Bill to date: ${bill_to_date:.2f}")
        display_menu()
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${bill_to_date:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break

        elif choice == 'c':
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    if distance <= 0:
                        print("Distance must be > 0")
                        continue

                    current_taxi.start_fare()  # Start new fare
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()

                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    bill_to_date += trip_cost

                except ValueError:
                    print("Invalid distance")

        else:
            print("Invalid option")


if __name__ == '__main__':
    main()