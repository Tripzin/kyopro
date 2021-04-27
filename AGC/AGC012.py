# A
N = int(input())
A = sorted(list(map(int,input().split())),reverse=True)
ans = 0

for i in range(1,N*2,2):
  ans += A[i]
print(ans)
