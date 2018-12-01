from itertools import cycle

with open('data.txt', 'r') as f:
    parsed = [int(line) for line in f]

# part 1
print("part one answer: ", sum(parsed))

# part 2
seen = set()
cur = 0

for num in cycle(parsed):
    cur += num

    if cur in seen:
        break

    else:
        seen.add(cur)


print("part two answer: ", cur)
