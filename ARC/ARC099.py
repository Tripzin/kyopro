import math
N,K = map(int,input().split(' '))
A = map(int,input().split(' '))

# 最初
N = N - K

if N == 0:
    print(1)
else:
    print(math.ceil(N/(K-1))+1)