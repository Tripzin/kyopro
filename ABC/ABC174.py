# X = int(input())
# print("Yes") if X >= 30 else print("No")
# import math
# N,D = map(int,input().split())

# cnt = 0
# for i in range(N):
#     x,y = map(int,input().split())

#     if math.sqrt(x**2+y**2) <= D:
#         cnt+=1
# print(cnt)


# while int(sev) < 2**63-1:
#     sev = int(sev)
#     if sev % K == 0:
#         print(len(str(sev)))
#         exit()
#     sev = str(sev) + "7"
# else:
#     print("-1")

# N = int(input())
# c = [None] * N
# r_cnt = 0
# for n,s in enumerate(input()):
#     c[n] = s
#     if s == "R":
#         r_cnt += 1
# w_cnt = 0
# for i in range(r_cnt):
#     if c[i] == "W":
#         w_cnt += 1
# print(w_cnt)

# K = int(input())
# a = 7 % K
# cnt = 1
# for k in range(K):
#     if a % K == 0:
#         print(cnt)
#         exit()
#     else:
#         cnt += 1
#         a = (a * 10 + 7) % K
# else:
#     print("-1")


N, K = map(int, input().split())
A = list(map(int, input().split()))


def f(n):
    cnt = 0
    for a in A:
            # a/nが偶数の場合
        if a % n == 0:
            cnt += a//n-1
        # a/nが奇数の場合
        else:
            cnt += a//n
    return True if K >= cnt else False


l = 0
r = max(A)
# 二分探索
while r - l > 1:
    m = (r+l)//2
    if f(m):
        r = m
    else:
        l = m
print(r)
