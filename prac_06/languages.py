"""
Programming Language Client Code
Estimate: 15 minutes
Actual:   13 minutes
"""

from programming_language import ProgrammingLanguage

def main():
    # Create ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Test __str__ method
    print(python)

    # Store in a list
    languages = [python, ruby, visual_basic]

    # Print dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
