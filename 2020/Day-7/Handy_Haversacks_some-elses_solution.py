with open('rules.txt', 'r') as text:
    bags = text.read().split(".\n")

# Part 1


def parentbag(childbag):                # function to find what bags can hold the childbag
    for parent in bags_dict:            # iterate through the different bags
        content = bags_dict[parent]     # what bags can be in parent bag
        if childbag in content:         # if the requested bag can be in parent bag
            parentbag(parent)           # recursion to see what bag can hold the parent bag
            bagset.add(parent)          # add bag to set of bags allowed to (eventually) hold childbag
    return


bags_dict = {}                          # initialize the dict
for bag in bags:                        # populate the dictionary
    bag = bag.replace(" bags", "").replace(" bag", "").replace(".", "")  # Remove text not required
    bag = bag.split(" contain ")        # split each entry into parent and child bag - note the spaces
    bags_dict[bag[0]] = bag[1]          # populate the dict. Key: parent, value: child

bagset = set()
parentbag("shiny gold")
print("Part 1: The amount of different coloured bags that can hold a shiny gold bag: " + str(len(bagset)))
