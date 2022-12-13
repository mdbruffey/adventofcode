def score_round(string):
    tie_conditions = ("A X", "B Y", "C Z")
    win_conditions = ("A Y", "B Z", "C X")
    lose_conditions = ("A Z", "B X", "C Y")
    score = ord(string[2]) - 87
    if string[:3] in tie_conditions:
        return score + 3
    if string[:3] in win_conditions:
        return score + 6
    return score

with open("input.txt") as file:
    rounds = file.readlines()

round_results = list(map(score_round, rounds))
print(sum(round_results))
