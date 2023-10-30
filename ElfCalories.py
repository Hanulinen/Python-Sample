# In this puzzle we receive an input file containing elf inventory calorie values separated by empty lines
# We need to work out which elf has the most calories stored in their inventory

# Open the input file
f = open("puzzleInput.txt", "r")

# Calories in the inventory currently being added
currentElfInventory = 0
# List of totals
elfTotals = []

# We go through every item in the list, adding items together for the total value. 
# If we notice an empty line, we know we have finished iterating through the current inventory
# We append the total to a list and null the total for the next inventory
for l in f:
    if l == "\n":
        elfTotals.append(currentElfInventory)
        currentElfInventory = 0
    else:
        currentElfInventory = currentElfInventory + int(l)

# We sort the elfTotals and add up the 3 largest
elfTotals.sort()
topThree = elfTotals[len(elfTotals)-1] + elfTotals[len(elfTotals)-2] + elfTotals[len(elfTotals)-3]

# Print the answer to the first puzzle
print(elfTotals[len(elfTotals)-1])

# print the answer to the second puzzle
print(topThree)