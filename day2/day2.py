# Advent Code - Day 2
# By: http://github.com/fakeforsure
# On: December 2, 2024

# Imports
import pathlib
folder_of_code = pathlib.Path(__file__).parent.resolve()
file = open(f"{folder_of_code}/adventcode_day2.txt") ### Load file

# Setup the count
count = 0

# Check if each line are either increasing or decreasing safely
for line in file:
    '''PART 1'''
    # Setup the variables
    numbers = list(map(int, line.strip().split())) ### Convert to list of int

    # Let's assume the line is increasing and decreasing by default
    is_increasing = True
    is_decreasing = True

    # Check if the line is increasing or decreasing by a certain number
    for i in range(len(numbers) - 1):
        # Check if the difference is between 1 and 3
        difference = numbers[i + 1] - numbers[i]
        if not (1 <= difference <= 3): ### If not in range, not increasing
            is_increasing = False
        if not (-3 <= difference <= -1): ### If not in range, not decreasing
            is_decreasing = False

    # If increasing or decreasing, add 1, else nothing happens
    if is_increasing or is_decreasing:
        count += 1
        continue ### Skip to PART 2 since the line is safe!

    '''PART 2'''
    # Check and remove each level to see if the line is safe
    safe = False

    # Check if the line is increasing or decreasing by a certain number if safe
    for i in range(len(numbers)):
        # Assume True by default again
        is_increasing = True
        is_decreasing = True

        # Remove the level
        temp = numbers[:i] + numbers[i + 1:]

        # Check if the line is increasing or decreasing by a certain number
        for j in range(len(temp) - 1):
            if not (1 <= temp[j + 1] - temp[j] <= 3): ### Not increasing!
                is_increasing = False
            if not (-3 <= temp[j + 1] - temp[j] <= -1): ### Not decreasing!
                is_decreasing = False
        if is_increasing or is_decreasing:
            safe = True
            break  # Stop checking further removals if one works
    
    # If safe, add 1 to the count
    if safe:
        count += 1

# Print out the final count
print(count)

# Done :,)
# For some reason this took me 18 hours???
file.close()
