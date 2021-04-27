# ABC160_c

# K, N = map(int, input().split())
# A = list(map(int, input().split()))
# diff = []
# for i in range(N):
#     if A[i-1] > A[i]:
#         diff.append(A[i]-(A[i-1]-K))
#     else:
#         diff.append(A[i]-(A[i-1]))

# print(sum(sorted(diff)[:-1]))

# AGC014

# A, B, C = map(int, input().split())

# if A % 2 == 1 and B % 2 == 1 and C % 2 == 1:
#     print(0)
#     exit()
# elif A == B and B == C:
#     print('-1')
#     exit()
# else:
#     ans = 0
#     while A % 2 != 1 and B % 2 != 1 and C % 2 != 1:
#         a = B//2+C//2
#         b = C//2+A//2
#         c = A//2+B//2
#         A, B, C = a, b, c
#         ans += 1
# print(ans)


# 2020_D


N = int(input())
A = list(map(int, input().split()))

# N日目の最大の所持金
dp = [1000] + [0] * (N-1)
for i in range(1, N):
    dp[i] = dp[i-1]

    for j in range(i):
        # j日に買える最大の株数
        max_unit = dp[j] // A[j]
        # その場合の所持金の変化
        money = dp[j] + (A[i]-A[j])*max_unit
        dp[i] = max(money, dp[i])

print(dp[-1])
