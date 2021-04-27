# S = list(input())

# r_cnt = 0
# max_r_cnt = 0

# for s in S:
#     if s == "R":
#         r_cnt += 1

#     else:
#         r_cnt = 0
#     max_r_cnt = max(r_cnt, max_r_cnt)

# print(max_r_cnt)

import itertools
N = int(input())
L = list(map(int, input().split()))
if N < 3:
    print(0)
    exit()
cnt = 0
Ns = [i for i in range(len(L))]
com = itertools.combinations(Ns, 3)
# print(list(com))
for ns in itertools.combinations(Ns, 3):
    # print(ns)
    if (L[ns[0]] != L[ns[1]] and L[ns[1]] != L[ns[2]] and L[ns[2]] != L[ns[0]]) and (L[ns[0]] + L[ns[1]] > L[ns[2]]) and (L[ns[1]] + L[ns[2]] > L[ns[0]]) and (L[ns[2]] + L[ns[0]] > L[ns[1]]):
        # print(L[ns[0]], L[ns[1]], L[ns[2]])
        cnt += 1

print(cnt)
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(i+j+1, N):
#             if (L[i] != L[j] != L[k]) and (L[i] + L[j] > L[k]) and (L[j] + L[k] > L[i]) and (L[k] + L[i] > L[j]):
#                 cnt += 1
# print(cnt)


# import math
# X, K, D = map(int, input().split())
# ans = 10**16
# minc_floor = math.floor(abs(X)/D)
# minc_ceil = math.ceil(abs(X)/D)
# min_kaisuu = K
# # print(minc_ceil, minc_floor)
# if minc_ceil <= K:
#     for k in range(minc_floor, minc_ceil+1):
#         for flug in [-1, 1]:
#             if abs(X + flug*k*D) < abs(ans):
#                 ans = abs(X + flug*k*D)

#                 # print("ans" + str(ans))
#                 min_kaisuu = k
#                 # print(min_kaisuu)
#     if (K-min_kaisuu) % 2 != 0:
#         ans = min(abs(ans+D), abs(ans-D))
# else:
#     # ans = min(ans+K*D), abs(ans-K*D))
#     if abs(X+K*D) > abs(X-K*D):
#         ans = X-K*D
#     else:
#         ans = X+K*D
# # print(min_kaisuu)
# print(abs(ans))


if A != B != C:

if A != B and B != C and C != A:
