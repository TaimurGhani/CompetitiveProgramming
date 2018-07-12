scan = [int(i) for i in input().split(" ")]
divisor = scan[0]
check = (divisor+1)*100
numbers = []
roundUp = []
result = 0;
for i in range(100,check, 100):
    if (round(i/divisor) > i/divisor):
        numbers.append((round(i/divisor), "u", i//100))
        roundUp.append(i//100)
    else:
        numbers.append((round(i/divisor), "d", i//100))
print (numbers)
print(roundUp)
survey = [int(i) for i in input().split(" ")]
for i in range(divisor - len(survey)):
    survey.append(0)
print(survey)
people = divisor - len(survey)
start = 1
ruInd = 0
while (start != people and ruInd != len(roundUp)):
    for i in range(len(survey)):
        print(survey[i])
        if (survey[i] + start == roundUp[ruInd]):
            survey[i] += start
            break;
        else:
            start += 1
            #break;
    ruInd += 1
print(survey)




