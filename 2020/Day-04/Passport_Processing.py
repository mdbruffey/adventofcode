def get_passports(raw_data):
    passports = []
    passport = {}
    for line in raw_data:
        if line == "\n":
            passports.append(passport)
            passport = {}
        else:
            while ":" in line:
                index_c = line.find(":")
                key = line[:index_c]
                line = line[index_c+1:]
                index_s = line.find(" ")
                data = line[:index_s]
                line = line[index_s+1:]
                passport[key] = data
    passports.append(passport)
    return passports

def passport_verified(passport):
    required_keys = ["byr",
                     "iyr",
                     "eyr",
                     "hcl",
                     "hgt",
                     "ecl",
                     "pid"]
    for key in required_keys:
        if key not in passport.keys():
            return False
    return True

def passport_validated(passport):
    
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    if int(passport["byr"]) not in range(1920, 2003):
        print(f"Rejected, bad birth year: {passport['byr']}")
        return False
    
    if int(passport["iyr"]) not in range(2010, 2021):
        print(f"Rejected, bad issue year: {passport['iyr']}")
        return False
    
    if int(passport["eyr"]) not in range(2020, 2031):
        print(f"Rejected, bad expiry year: {passport['eyr']}")
        return False
    
    if passport["hgt"][-2:] == "cm":
        try:
            if int(passport["hgt"][:-2]) not in range(150, 194):
                print(f"Rejected, bad height: {passport['hgt'][:-2]}cm")
                return False
        except Exception:
            return False
    elif passport["hgt"][-2:] == "in":
        try:
            if int(passport["hgt"][:-2]) not in range(59, 77):
                print(f"Rejected, bad height: {passport['hgt'][:-2]}in")
                return False
        except Exception:
            return False
    else:
        print(f"Rejected, bad height unit: {passport['hgt'][-2:]}")
        return False
    
    if len(passport["hcl"]) != 7 or passport["hcl"][0] != "#":
        print(f"Rejected, bad haircolor: {passport['hcl']}")
        return False

    if len(passport["ecl"]) != 3 or passport["ecl"] not in eye_colors:
        print(f"Rejected, bad eye color: {passport['ecl']}")
        return False

    if len(passport["pid"]) != 9:
        print(f"Rejected, bad pid: {passport['pid']}")
        return False

    return True
    
                     
with open('passport_data.txt') as file:
    raw_data = file.readlines()

passports = get_passports(raw_data)
count = 0
for passport in passports:
    if passport_verified(passport):
        if passport_validated(passport):
            count += 1

print(count)
