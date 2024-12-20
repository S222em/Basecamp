# Unix-based operating systems usually include a tool named head.
# It displays the first 10 lines of a file whose name is provided as a command line parameter.
# Write a Python program that provides the same behavior.
#
# Criteria:
# Use sys.argv to get the file from running
# Input example (correct):
# python3 head.py randomfile.txt
#
# Output example (correct):
# this is line #1
# this is line #2
# this is line #3
# this is line #4
# this is line #5
# this is line #6
# this is line #7
# this is line #8
# this is line #9
# this is line #10
# Input example (error):
# blanc
#
# Output example (error):
# Error reading file: "blanc"
import sys


def main(file_name):
    try:
        with open(file_name) as file:
            lines = [next(file) for _ in range(10)]
            print("".join(lines))
    except IOError:
        print(f'Error reading file: "{file_name}"')


if __name__ == "__main__":
    main(sys.argv[1])
