def thing(string, debug=False):
    g1,g2 = string.split(",")
    r1 = [*range(int(g1[:g1.find("-")]),int(g1[g1.find("-")+1:])+1)]
    r2 = [*range(int(g2[:g2.find("-")]),int(g2[g2.find("-")+1:])+1)]
    r1 = "," + ",".join(list(map(str,r1))) + ","
    r2 = "," + ",".join(list(map(str,r2))) + ","
    if debug:
        print(r1, r2)
    if r1 in r2 or r2 in r1:
        return True
    else:
        return False

def other_thing(string, debug=False):
    g1,g2 = string.split(",")
    r1 = [*range(int(g1[:g1.find("-")]),int(g1[g1.find("-")+1:])+1)]
    r2 = [*range(int(g2[:g2.find("-")]),int(g2[g2.find("-")+1:])+1)]
    intersection = list(set(r1).intersection(r2))
    intersection.sort()
    if debug:
        print(intersection)
    if intersection == r1 or intersection == r2:
        return True
    else:
        return False
    

with open('input.txt') as file:
    data = file.read().split("\n")
    
count = 0
for line in data:
    if thing(line):
        count += 1

print(count)

count = 0
for line in data:
    if other_thing(line):
        count += 1

print(count)
