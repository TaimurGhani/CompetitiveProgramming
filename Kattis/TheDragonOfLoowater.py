while (True):
    dragonNum, knightNum = input().split(' ')
    dragonNum, knightNum = int(dragonNum), int(knightNum)
    if (dragonNum == 0 and knightNum == 0):
        break;
    dragons = []
    knights = []
    for _ in range(dragonNum):
        dragons.append(int(input()))
    for _ in range(knightNum):
        knights.append(int(input()))
    dragons, knights = sorted(dragons), sorted(knights)

    def cost(dragons, knights):
        result = 0
        iD = 0
        iK = 0
        if (len(dragons) > len(knights)):
            return -1
        while (iD < len(dragons) and iK < len(knights)):
            if (dragons[iD] <= knights[iK]):
                result += knights[iK]
                iD += 1
                iK += 1
            else:
                iK += 1
        if (iD == len(dragons)):
            return result
        else:
            return -1

    ans = cost(dragons, knights)
    if ( ans == -1 ):
        print("Loowater is doomed!")
    else:
        print(ans)
