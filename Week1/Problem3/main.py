# Write a program that asks the user to enter the width and length of a room.
# Once the values have been read, your program should compute and display the area of the room.
#
# Criteria:
# The length and the width will be entered as floating point numbers
# Input example:
# Width: 5
# Length: 5.5
#
# Output example:
# The Area of the Room: 27.5
import re


def validate_and_convert_to_float(to_convert: str):
    if not re.fullmatch("\d+.\d+", to_convert):
        print("Please enter a valid decimal number")
        exit()

    return float(to_convert)


width = validate_and_convert_to_float(input("Width: "))
length = validate_and_convert_to_float(input("Length: "))

print(f"The Area of the Room: {width * length}")
