# Advent Code - Day 3
# By: http://github.com/fakeforsure
# On: December 2, 2024

# Imports
import pathlib
import re
folder_of_code = pathlib.Path(__file__).parent.resolve()
file = open(f"{folder_of_code}/adventcode_day3.txt") ### Load file

'''PART 1'''
# Search the file for every time there is mul(num,num) exactly and no other way
pattern = re.compile(r"mul\((\d+),(\d+)\)") ### I used documentation to help me
total_sum = 0

# Loop through the file and find all the matches
for line in file:
    matches = pattern.findall(line)
    for match in matches:
        num1, num2 = map(int, match)
        total_sum += num1 * num2

# Print the total sum
print(total_sum)

'''PART 2'''
# Reset file
file.seek(0)

# Set some variables before the loop
pattern = re.compile(r"((mul\((\d+),(\d+)\)|do\(\)|don't\(\)))")
### I used documentation and YouTube to help and explain to me here 😭😭😭
total_sum = 0
enabled = True

# Loop through the file and find all the matches according to the conditions
for matchline in re.findall(pattern, file.read()):
    match = matchline[0]
    if match.startswith("do()"):
        enabled = True
    elif match.startswith("don't()"):
        enabled = False
    elif enabled:
        num1, num2 = map(int, re.findall(r"\d+", match))
        total_sum += num1 * num2

# Print the total sum
print(total_sum)

# Done :,)
file.close()
