numPeople = int(input())
check = [int(i) for i in input().split(" ")]
nums = sorted(check, reverse=True)
nums.insert(0, -1)
nums.append(-1)
flag = True
for j in range(1, len(nums)-1):
    if (nums[j-1] != nums[j] and nums[j+1] != nums[j]):
        remember = nums[j]
        flag = False;
        break;
if (flag):
    print("none")
else:
    print(check.index(remember) + 1)
