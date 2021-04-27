from collections import deque
n = int(input())
a = input().split()
b = deque()


for i in range(0,n):
    if i % 2 == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])
if n % 2 != 0:
    b.reverse()

print(*b)

