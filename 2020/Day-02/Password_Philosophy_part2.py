def password_is_valid(data):
    hyphen_index = data[0].find("-")
    first_index = int(data[0][:hyphen_index])
    second_index = int(data[0][hyphen_index+1:])
    character = data[1][0]
    password = data[2]
    if password[first_index-1] == password[second_index-1]:
        return False
    else:
        return password[first_index-1] == character or password[second_index-1] == character

with open('day2_passwords.txt') as file:
    passwords = file.readlines()

count = 0
for password in passwords:
    if password_is_valid(password.split()):
        count += 1

print(count)
