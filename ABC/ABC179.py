# A
# S = input()

# if S[-1] == "s":
#   print(S + "es")
# else :
#   print(S + "s")

# B
# N = int(input())
# F_S = [list(map(int,input().split())) for _ in range(N)]

# cnt = 0
# for f,s in F_S:
#   if cnt >= 3:
#     break
#   if f == s:
#     cnt += 1
#   else:
#     cnt = 0
# if cnt >= 3:
#   print("Yes")
# else:
#   print("No")

# C
# import math
# N = int(input())
# cnt = 0
# for a in range(1,N):
#   for b in range(a,math.ceil(N/a)):
#     c = N - a * b
#     if c <= 0:
#       break
#     else:
#       if a == b:
#         cnt += 1
#       else :
#         cnt += 2
# print(cnt)


# print(cnt)

# N,K = map(int,input().split())
# L_R = [list(map(int,input().split())) for _ in range(K)]
# mod = 998244353


# D

# 繰り返しの始まり + 繰り返し + 途中で終わった繰り返し分
N,X,M = map(int,input().split())
p = [0] * (M+2)
sum = [0] * (M+2)
p[X] = 1
sum[1] = X

repeat_start = 0
repeat_end = 0

for i in range(2,N+1):
  X = (X**2) % M
  if p[X] != 0:
    repeat_start = p[X]
    repeat_end = i
    break
  else:
    sum[i] = sum[i-1] + X
    p[X] += i

if repeat_start == 0:
  print(sum[N])
else:
  repeat_cnt,mod=divmod(N-repeat_start+1,repeat_end-repeat_start)
  print(repeat_cnt*(sum[repeat_end-1]-sum[repeat_start-1]) + sum[repeat_start+mod-1])







      

