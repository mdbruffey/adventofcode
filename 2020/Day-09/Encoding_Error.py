def find_sum(numbers, total):
    length = len(numbers)
    for i in range(0, length):
        for j in range(i+1, length):
            if numbers[i]+numbers[j] == total:
                return True
    return False

def decrypt(numbers, preamble_len):
    for i in range(preamble_len, len(numbers)):
        valid = find_sum(numbers[i - preamble_len: i],numbers[i])
        if not valid:
            return numbers[i]
    return 0

with open("input.txt") as file:
    numbers = list(map(int,file.read().split("\n")))

key = decrypt(numbers, 25)
print(key)

for i in range(0, len(numbers)):
    count = 0
    j = i
    while count < key:
        count += numbers[j]
        j += 1
    if count == key:
        sequence = numbers[i:j]
        encryption_strength = min(sequence) + max(sequence)
        break

print(encryption_strength)
