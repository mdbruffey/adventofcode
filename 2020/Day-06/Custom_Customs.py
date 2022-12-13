def get_families(data):
    families = []
    string = ""
    for line in data:
        if line == "\n":
            families.append(set(string))
            string = ""
        else:
            string += line.strip('\n')
            
    families.append(set(string))
    return families

with open("customs_qs.txt") as file:
    raw_data = file.readlines()

families = get_families(raw_data)
print(sum(list(map(len, families))))
