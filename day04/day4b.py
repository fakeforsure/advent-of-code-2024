# Advent Code - Day 4b
# By: http://github.com/fakeforsure
# On: December 4, 2024

# Imports
import pathlib
folder_of_code = pathlib.Path(__file__).parent.resolve()
file_index = f"{folder_of_code}/adventcode_day4.txt"
file = open(file_index).readlines()

'''PART 1''' ### See day4a.py for the first part of the code

'''PART 2''' ### Huge thanks to the subreddit for help (hints) on this part
# Function to find how much MAS appears in the file in X shape
def find_mas(file):
    data = open(file_index).read().strip()
    regrid = data.split('\n')
    rerow = len(regrid)
    recol = len(regrid[0])
    mas_count = 0

    # Function to search for a word in the grid using x, y
    for row in range(rerow):
        for col in range(recol):
            if row+2 < rerow and col+2 < recol and regrid[row][col] == 'M' \
and regrid[row+1][col+1] == 'A' and regrid[row+2][col+2] == 'S' and \
regrid[row+2][col] == 'M' and regrid[row][col+2] == 'S':
                mas_count += 1
            if row+2 < rerow and col+2 < recol and regrid[row][col] == 'M' \
and regrid[row+1][col+1] == 'A' and regrid[row+2][col+2] == 'S' and \
regrid[row+2][col] == 'S' and regrid[row][col+2] == 'M':
                mas_count += 1
            if row+2 < rerow and col+2 < recol and regrid[row][col] == 'S' \
and regrid[row+1][col+1] == 'A' and regrid[row+2][col+2] == 'M' and \
regrid[row+2][col] == 'M' and regrid[row][col+2] == 'S':
                mas_count += 1
            if row+2 < rerow and col+2 < recol and regrid[row][col] == 'S' \
and regrid[row+1][col+1] == 'A' and regrid[row+2][col+2] == 'M' and \
regrid[row+2][col] == 'S' and regrid[row][col+2] == 'M':
                mas_count += 1
    return mas_count

'''MAIN'''
# Get the result
mas_count = find_mas(file)
print(f"MAS count: {mas_count}")

# Done :,)