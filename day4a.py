# Advent Code - Day 4a
# By: http://github.com/fakeforsure
# On: December 3, 2024

# Imports
import pathlib
folder_of_code = pathlib.Path(__file__).parent.resolve()
file_index = f"{folder_of_code}/adventcode_day4.txt"
file = open(file_index).readlines()

'''PART 1''' ### This part wasn't too hard
# Function to find how much XMAS appears in the file
def find_xmas(file):
    grid = [list(line.strip()) for line in file]
    row = len(grid)
    col = len(grid[0])
    XMAS = 'XMAS'
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), \
(-1, 1)]
    xmas_count = 0

    # Function to search for a word in the grid using x, y
    def search_from(x, y, dx, dy, word):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < row and 0 <= ny < col) or grid[nx][ny] != word[i]:
                return False
        return True

    # Call the function to search for XMAS in the grid for range in x, y
    for x in range(row):
        for y in range(col):
            for dx, dy in directions:
                if search_from(x, y, dx, dy, XMAS):
                    xmas_count += 1
    return xmas_count

'''PART 2''' ### See day4b.py for the rest of the code

'''MAIN'''
# Get the result
xmas_count = find_xmas(file)
print(f"XMAS count: {xmas_count}")

# Done :)