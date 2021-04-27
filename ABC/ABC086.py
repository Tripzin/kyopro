a, b = input().split()
N = int(a+b)
for n in range(N):
    if n*n == N:
        print("Yes")
        break
else:
    print("No")
