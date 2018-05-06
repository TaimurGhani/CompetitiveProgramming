def sumDigitis(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
    return s

def recur (num):
    if (num == 0):
        return 0
    else:
        return ((num%10)*(num%10-1))//2 + 10*recur(num//10) + (num//10)*45  + (num%10)*(sumDigitis(num//10))

loop = int(input())
for _ in range(loop):
    a, b = [int(i) for i in input().split(' ')]
    print(int(recur(b) - recur(a)) + sumDigitis(b))