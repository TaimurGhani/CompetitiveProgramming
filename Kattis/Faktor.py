parts = input().split(' ')
publish = int(parts[0])
impactFactor = int(parts[1])

citations = (impactFactor - 1) * publish + 1
print(citations)