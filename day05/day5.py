# Advent Code - Day 5
# By: http://github.com/fakeforsure
# On: December 5, 2024

# Imports
import pathlib
folder_of_code = pathlib.Path(__file__).parent.resolve()
file = open(f"{folder_of_code}/adventcode_day5.txt").read().split("\n\n")
bit_pageorder, bit_updates = file
bit_pageorder = bit_pageorder.split("\n")
bit_updates = [i.split(",") for i in bit_updates.split("\n")]

'''PART 1'''
# Separate the page order into a dictionary
pageorder = {}
for line in bit_pageorder:
    x, y = line.split("|")
    if x in pageorder:
        pageorder[x].append(y)
    else:
        pageorder[x] = [y]

# Function to check if the rule is being met
def rule_met(x):
    for i, rule in enumerate(x):
        if rule not in pageorder:
            continue
        for j in pageorder[rule]:
            if j in x:
                if x.index(j) < i:
                    return 0
    return int(x[int((len(x)-1)/2)])

# Find the sum of the mid number of the correct updates that follow the rule
result = 0
not_met = []
for num in bit_updates:
    x = rule_met(num)
    result += x
    if x == 0:
        not_met.append(num)

# Print the result
print(result)

'''PART 2'''
# Check if the rule not being met will actually work if rearranged
def will_it_work(x):
    while True:
        for i, rule in enumerate(x):
            if rule not in pageorder:
                continue
            for j in pageorder[rule]:
                if j in x:
                    if x.index(j) < i:
                        lil_bit = x.index(j)
                        x[lil_bit], x[i] = rule, j
                        new_rule = rule_met(x)
                        if new_rule != 0:
                            return new_rule
                        else:
                            break

# Find the sum of the mid number of the correct updates that follow the rule
result2 = 0
for num in not_met:
    x = will_it_work(num)
    result2 += x

# Print the result
print(result2)

# Done :)
