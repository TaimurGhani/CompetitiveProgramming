loop = int(input())
for _ in range(loop):
    s1 = input()
    s2 = input()
    result = []
    for char1, char2 in zip(s1, s2):
        if (char1 == char2):
            result.append(".")
        else:
            result.append("*")
    print(s1)
    print(s2)
    print(''.join(result), end = "\n\n")
