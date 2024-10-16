# Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
#
# Criteria:
# The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
# Include appropriate headings on your columns.
# The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the internet .
# Input example:
# No input is given
#
# Output example:
# °C °F
# 10 50
# 20 68

print("°C °F")

for i in range(11):
    celsius = i * 10
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius} {fahrenheit:.0f}")
