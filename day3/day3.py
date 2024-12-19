import re

f = open("input3.txt", "r")

matches = re.findall(r"mul\((\d\d?\d?),(\d\d?\d?)\)|(do\(\)|don't\(\))", f.read())

do = True
total = 0
for match in matches:
    if match[2] == "don't()":
        do = False
        continue
    elif match[2] == "do()":
        do = True
        continue

    if do:
        total += int(match[0]) * int(match[1])

print(total)
