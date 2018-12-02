from collections import Counter

# part one
two = 0
three = 0

with open('2.txt', 'r') as f:
    for line in f:
        counts = Counter(line)

        if any(x == 2 for x in counts.values()):
            two += 1

        if any(x == 3 for x in counts.values()):
            three += 1

print("checksum: ", two * three)

# part two
def check_strings(s1, s2):
    diffs = 0

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diffs += 1

            if diffs > 1:
                return False

    return True

def find_id(lines):
    for str1 in lines:
        for str2 in lines:
            if str1 != str2 and check_strings(str1, str2):
                return str1, str2

    return None,None


with open('2.txt', 'r') as f:
    lines = f.readlines()

# lol, bruteforce
id1, id2 = find_id(lines)
final_id = ''.join([c1 if c1 == c2 else '' for (c1,c2) in zip(id1, id2)])
print("id: ", final_id)
