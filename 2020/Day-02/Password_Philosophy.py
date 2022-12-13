def password_is_valid(data):
    hyphen_index = data[0].find("-")
    char_min = int(data[0][:hyphen_index])
    char_max = int(data[0][hyphen_index+1:])
    character = data[1][0]
    password = data[2]
    count = password.count(character)
    return count >= char_min and count <= char_max

with open('day2_passwords.txt') as file:
    passwords = file.readlines()

count = 0
for password in passwords:
    if password_is_valid(password.split()):
        count += 1

print(count)
