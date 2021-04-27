# C

# X = int(input())
# dp = [True] + [False] * (X)

# if X < 106:
#   if 100 <= X <= 105:
#     print(1)
#     exit()
#   else:
#     print(0)
#     exit()


# # 100~105円はyes
# for i in range(100,106):
#   dp[i] = True

# for i in range(106,X+1):
#   for j in range(100,106):
#     if dp[i-j] == True:
#       dp[i] = True
#       break

# print(1 if dp[X] == True else 0)