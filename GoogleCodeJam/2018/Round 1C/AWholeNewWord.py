from copy import deepcopy
loop = int(input())
for _ in range(loop):
    numW, lenW = [int(i) for i in input().split(" ")]
    words = []
    for i in range(numW):
        word = input()
        words.append(list(word))
    a = deepcopy(words)
    w = deepcopy(words[0])
    flag = False
    for k in range(1, numW):
        for j in range(lenW):
            testW = deepcopy(w)
            testW[j] = words[k][j]
            if (testW != words[k] and (testW in a)==False):
                print("Case #" + str(_+1) + ": " + ''.join(testW))
                flag = True
                break;
        if (flag):
            break;
    if (flag == False):
        print("Case #" + str(_+1) + ": -")







# lst = []
# words =[]
# for i in range(numW):
#     word = input()
#     words.append(word)
#
# for j in range(lenW):
#     dict = {}
#     for w in words:
#         if (w[j] in dict):
#             dict[w[j]] += 1
#         else:
#             dict[w[j]] = 1
#     lst.append(dict)
# def check(lst):
#     if (len(lst) == 1):
#         return "-"
#     for k in range(lst-1):
#         if (len(k[i]) != len(k[i+1])):
#             return "-"



