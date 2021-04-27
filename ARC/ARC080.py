N=int(input())
A = map(int,input().split(' '))

o = 0
s = 0
f = 0
for a in A:

    if a % 2 == 0:
        if a % 4 == 0:
            f += 1
        else:
            s += 1
    else:
        o += 1
if s == 0:
    if f >= o-1:
        print("Yes")
    else:
        print("No")
else:
    if f >= o:
        print("Yes")
    else:
        print("No")

