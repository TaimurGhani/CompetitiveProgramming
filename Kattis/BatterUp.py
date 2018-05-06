numBats = int(input())
parts = input().split()
parts = [int(i) for i in parts if int(i) != -1]
print(sum(parts)/len(parts))
