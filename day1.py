# Advent Code - Day 1
# By: Luc Bassaler-Merpillat
# On: November 30, 2024

# Imports
import pathlib
folder_of_code = pathlib.Path(__file__).parent.resolve()
file = open(f"{folder_of_code}/adventcode_day1.txt")

# Create list
lines_list = []
for line in file:
    words = line.strip().split()
    lines_list.append(words)

# Sub num to other num
results_list = []
for word in lines_list:
    result = int(word[0]) - int(word[1])
    results_list.append(abs(result)) ### Absolute value of the result

# Sum of all results
sum_results = sum(results_list)
print(sum_results)

# Done! :)
file.close()