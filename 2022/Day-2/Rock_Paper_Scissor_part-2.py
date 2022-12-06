def score_round(string):
    tie_conditions = ("A A", "B B", "C C")
    win_conditions = ("A B", "B C", "C A")
    score = ord(string[2]) - 64
    if string[:3] in tie_conditions:
        return score + 3
    if string[:3] in win_conditions:
        return score + 6
    return score

def calculate_move(string):
    if string[2] == "X":
        adjusted_ascii = ord(string[0]) - 66
        if adjusted_ascii < 0:
            adjusted_ascii += 3
        move = chr(adjusted_ascii+65)
    elif string[2] == "Y":
        move = string[0]
    else:
        adjusted_ascii = ord(string[0]) - 64
        if adjusted_ascii > 2:
            adjusted_ascii -= 3
        move = chr(adjusted_ascii+65)
        
    return f"{string[0]} {move}"

with open("input.txt") as file:
    data = file.readlines()

rounds = list(map(calculate_move, data))
round_results = list(map(score_round, rounds))
print(sum(round_results))
