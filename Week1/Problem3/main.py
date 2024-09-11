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

width = input("Width: ")
length = input("Length: ")

try:
    width = float(width)
    length = float(length)
    print(f"The Area of the Room: {width * length}")
except ValueError:
    print("Please enter a valid decimal number")
