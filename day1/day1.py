# Advent Code - Day 1
# By: http://github.com/fakeforsure
# On: November 30, 2024

# Imports
import pathlib
folder_of_code = pathlib.Path(__file__).parent.resolve()
file = open(f"{folder_of_code}/adventcode_day1.txt") ### Load file

'''PART 1'''
# Create two lists: one for the right side and one for the left side
right_side = []
left_side = []
for line in file:
    word = line.strip().split()
    right_side.append(int(word[1]))
    left_side.append(int(word[0]))

#Sort from smallest to largest, literally built in function
right_side.sort()
left_side.sort()

# Find the distance between the two sides
distance = 0
for i in range(len(right_side)): ### Len of any side is the same tbh
    distance += abs(right_side[i] - left_side[i])

# Print distance
print(distance)

'''PART 2'''
# Find how many times the num on the left appears in the right side
similar = 0
for num in left_side:
    if num in right_side:
        similar += num * right_side.count(num)

# Print the sum of similar numbers
print(similar)

# Done :)
file.close()
