nums = sorted([int(i) for i in input().split(" ")])
letters = list(input())
result = []
for letter in letters:
    if letter == 'A':
        result.append(str(nums[0]))
    elif letter == 'B':
        result.append(str(nums[1]))
    else:
        result.append(str(nums[2]))
print(" ".join(result))
