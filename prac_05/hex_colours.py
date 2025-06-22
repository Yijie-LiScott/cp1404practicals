"""
Hex Colour Lookup Program
Allows user to look up hexadecimal colour codes by name (case-insensitive).
"""

# Constant dictionary of colour names and their hex codes
COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

print("Hex Colour Lookup")
colour_name = input("Enter colour name (blank to quit): ").strip().lower()
while colour_name != "":
    hex_code = COLOUR_CODES.get(colour_name)
    if hex_code:
        print(f"The hex code for {colour_name} is {hex_code}")
    else:
        print("Invalid colour name.")
    colour_name = input("Enter colour name (blank to quit): ").strip().lower()
