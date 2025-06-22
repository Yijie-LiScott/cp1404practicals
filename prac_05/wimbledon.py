"""
Wimbledon Champions Summary
Estimate: 35 minutes
Actual:   52 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    records = load_wimbledon_data(FILENAME)
    champion_to_wins = count_champions(records)
    countries = extract_countries(records)
    display_champion_wins(champion_to_wins)
    display_countries(countries)


def load_wimbledon_data(filename):
    """Read Wimbledon data file and return a list of records."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def count_champions(records):
    """Count number of wins per champion, return as a dictionary."""
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def extract_countries(records):
    """Extract unique countries from the records."""
    return sorted({record[1] for record in records})


def display_champion_wins(champion_to_wins):
    """Display each champion and their number of wins."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items()):
        print(f"{champion} {wins}")


def display_countries(countries):
    """Display the sorted list of countries as a string."""
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()