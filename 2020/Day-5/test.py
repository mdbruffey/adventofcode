def convert_thing(string):
    row = 0
    column = 0
    for i, char in enumerate(string[:-3]):
        if char == "B":
            row += pow(2, 6-i)
    for i, char in enumerate(string[-3:]):
        if char == "R":
            column += pow(2, 2-i)
    print(f"{string}: {8*row + column}")
    return 8*row + column

while(True):
    convert_thing(input("Boarding Pass:"))
