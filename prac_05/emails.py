"""
Emails - Store email-to-name mapping
Estimate: 25 minutes
Actual:   21 minutes
"""

def main():
    """Store emails and names in a dictionary, and display them at the end."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ("", "y"):
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """
    Extract a name from the email address.
    E.g., "lindsay.ward@jcu.edu.au" -> "Lindsay Ward"
    """
    username = email.split('@')[0]
    parts = username.replace('.', ' ').replace('_', ' ').split()
    return ' '.join(parts).title()



main()