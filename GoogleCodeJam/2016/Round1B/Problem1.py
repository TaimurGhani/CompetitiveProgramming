import collections
f = open("output.txt", "w")
a = open("A-large-practice.in", "r")
loop = int(a.readline())
for i in range(loop):
    sP = a.readline()
    letters = collections.Counter(sP)
    result = []
    while (letters['Z'] != 0):
        result.append(0)
        letters["Z"] -= 1
        letters["E"] -= 1
        letters["R"] -= 1
        letters["O"] -= 1
    while (letters['U'] != 0):
        result.append(4)
        letters["F"] -= 1
        letters["O"] -= 1
        letters["U"] -= 1
        letters["R"] -= 1
    while (letters['G'] != 0):
        result.append(8)
        letters["E"] -= 1
        letters["I"] -= 1
        letters["G"] -= 1
        letters["H"] -= 1
        letters["T"] -= 1
    while (letters['X'] != 0):
        result.append(6)
        letters["S"] -= 1
        letters["I"] -= 1
        letters["X"] -= 1
    while (letters['F'] != 0):
        result.append(5)
        letters["F"] -= 1
        letters["I"] -= 1
        letters["V"] -= 1
        letters["E"] -= 1
    while (letters['W'] != 0):
        result.append(2)
        letters["T"] -= 1
        letters["W"] -= 1
        letters["O"] -= 1
    while (letters['V'] != 0):
        result.append(7)
        letters["S"] -= 1
        letters["E"] -= 1
        letters["V"] -= 1
        letters["E"] -= 1
        letters["N"] -= 1
    while (letters['R'] != 0):
        result.append(3)
        letters["T"] -= 1
        letters["H"] -= 1
        letters["R"] -= 1
        letters["E"] -= 1
        letters["E"] -= 1
    while (letters['I'] != 0):
        result.append(9)
        letters["N"] -= 1
        letters["I"] -= 1
        letters["N"] -= 1
        letters["E"] -= 1
    while (letters['O'] != 0):
        result.append(1)
        letters["O"] -= 1
        letters["N"] -= 1
        letters["E"] -= 1
    result.sort()
    f.write("Case #" + str(i + 1) + ": " + ''.join([str(num) for num in result]) + "\n")
f.close()
a.close()