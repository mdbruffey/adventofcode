def get_families(data):
    families = []
    string = ""
    members = 0
    for line in data:
        if line == "\n":
            families.append((string,members))
            string = ""
            members=0
        else:
            string += line.strip('\n')
            members += 1
            
    families.append((string,members))
    return families

def check_questions(family):
    string, members = family
    count = 0
    for char in set(string):
        if string.count(char) == members:
            count += 1

    return count
            

with open("customs_qs.txt") as file:
    raw_data = file.readlines()

families = get_families(raw_data)
print(sum(list(map(check_questions, families))))

