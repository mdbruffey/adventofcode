with open('input.txt') as file:
    data = file.read().split("\n")
adapters = list(map(int, data))
adapters.append(0)
adapters.sort(reverse=True)

path_dict = {adapters[0]: 1}
for i, adapter in enumerate(adapters[1:]):
    paths = 0
    for j in range(0,3):
        try:
            dif = adapters[i-j] - adapter
        except IndexError:
            break
        if dif > 0 and dif < 4:
            paths += path_dict[adapters[i-j]]
            if dif == 3:
                break
    path_dict[adapter] = paths

print(path_dict[0])
    
    




