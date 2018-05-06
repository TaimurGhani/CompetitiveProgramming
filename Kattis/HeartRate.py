N = int(input())

for _ in range(N):
    b, p = input().split(' ')
    b = int(b)
    p = float(p)
    minABP = (b-1) * (60/p)
    calBPM = b * (60/p)
    maxABP = (b+1) * (60/p)
    print(minABP, calBPM, maxABP)