def find_2020(int_list):
    for i, first in enumerate(intl):
        for j, second in enumerate(intl[i+1:]):
            for third in intl[j+1:]:
                if first + second + third == 2020:
                    print(first*second*third)
                    return

        
with open("problem1.txt") as file:
    strl = file.readlines()
intl = list(map(int, strl))
find_2020(intl)
