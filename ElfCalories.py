# In this puzzle we receive an input file containing elf inventory calorie values separated by empty lines
# We need to work out which elf has the most calories stored in their inventory

# Open the input file
f = open("puzzleInput.txt", "r")

# Calories in the inventory currently being added
currentElfInventory = 0
# List of totals
elfTotals = []
# Index of the elf with the most calories
chunkiestElfIndex = 0
# Iterator for going through elfTotals
elfIterator = 0

# We go through every item in the list, adding items together for the total value. 
# If we notice an empty line, we know we have finished iterating through the current inventory
# We append the total to a list and null the total for the next inventory
for l in f:
    if l == "\n":
        elfTotals.append(currentElfInventory)
        currentElfInventory = 0
    else:
        currentElfInventory = currentElfInventory + int(l)

# We iterate through all the totals to find the highest total in the list
for i in elfTotals:
    if i > elfTotals[chunkiestElfIndex]:
        chunkiestElfIndex = elfIterator
    elfIterator += 1

# Print the highest total
print(elfTotals[chunkiestElfIndex])
  