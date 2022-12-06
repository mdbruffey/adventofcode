def convert_thing(string):
    string = string[:-1] #THERE IS A STUPID ENDLINE CHARACTER!!!!!!!!
    row = 0
    column = 0
    for i, char in enumerate(string[:-3]):
        if char == "B":
            row += 2**(6-i)
    for j, char in enumerate(string[-3:]):
        if char == "R":
            column += 2**(2-j)
    return (8*row) + column

with open('boarding_passes.txt') as file:
    bpasses = file.readlines()
    
pass_ids = list(map(convert_thing, bpasses))
pass_ids.sort()
for i in range(0, len(pass_ids)-1):
    if pass_ids[i+1] - pass_ids[i] != 1:
        print(f"Missing pass_id {pass_ids[i]+1}")
        break
