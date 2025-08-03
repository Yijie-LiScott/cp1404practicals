"""
CP1404/CP5632 Practical
Wikipedia API interaction using python library
"""

import wikipedia


def search_wikipedia(query):
    """Search Wikipedia for articles related to the query."""
    try:
        search_results = wikipedia.search(query)
        print(f"Search results for '{query}':")
        for i, result in enumerate(search_results, 1):
            print(f"{i}. {result}")
        return search_results
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation Error: {e.options}")
        return e.options
    except wikipedia.exceptions.WikipediaException as e:
        print(f"Wikipedia Error: {e}")
        return None


def get_page_summary(title):
    """Get the summary of a Wikipedia page by its title."""
    try:
        page = wikipedia.page(title)
        print(f"\nTitle: {page.title}")
        print(f"Summary:\n{page.summary}")
        return page.summary
    except wikipedia.exceptions.PageError:
        print(f"Page '{title}' does not exist.")
        return None
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation Error - Multiple options: {e.options}")
        return None


def main():
    """Main function to demonstrate Wikipedia API usage."""
    print("Wikipedia API Demo")

    # Search for a term
    search_term = input("Enter a term to search Wikipedia: ")
    results = search_wikipedia(search_term)

    if results:
        # Get summary of first result
        try:
            choice = int(input("Enter the number of the article you want to see: ")) - 1
            if 0 <= choice < len(results):
                get_page_summary(results[choice])
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()