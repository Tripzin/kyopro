# A
# N = int(input())

# if N % 100 == 0:
#   print(N//100)
# else :
#   print(N//100 + 1)
# B
# N,K = map(int,input().split())

# for _ in range(K):
#   if N % 200 == 0:
#     N //= 200
#   else:
#     N = int(str(N) + '200')

# print(N)

# C
from collections import Counter
from math import factorial
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

def func(x):
  x = int(x)
  return x % 200

N = int(input())
A = list(map(func,input().split()))

p       = 10 ** 9 + 7
N       = 10 ** 6  
fact    = [1, 1]  
factinv = [1, 1]  
inv     = [0, 1]  
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

countA = Counter(A)

cnt = 0
for count in countA.values():
  cnt += cmb(count,2,p)
print(int(cnt))