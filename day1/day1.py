f = open("input.txt", "r")

left = []
right = []

for line in f:
    split_line = line.strip("\n").split("   ")
    left.append(int(split_line.pop()))
    right.append(int(split_line.pop()))

f.close()

left.sort()
right.sort()

sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)


# part two!

right_index = 0
similarity_score = 0

for left_index, num in enumerate(left):
    this_count = 0
    while right[right_index] < num:
        right_index += 1

    if right[right_index] > num:
        continue

    if right[right_index] == num:
        count_this_number = right_index
        while num == right[count_this_number]:
            count_this_number += 1
            this_count += 1
    similarity_score += num * this_count

print(similarity_score)
