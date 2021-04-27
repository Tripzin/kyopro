# x = int(input())

# print(1) if x == 0 else print(0)

# a,b,c,d = map(int,input().split())

# print(max(a*c,a*d,b*c,b*d))

# def dekai():
#   return (10**9)+7

# def kaizyo(N):

#   if N == 1:
#     return 0
#   else:
#     ans = 1
#     for i in range(1,N+1):
#       ans *= i
#     return ans
# # C

# N = int(input())
# if N == 1:
#   print(0)
#   exit()
# # x 0,9 igai
# ans = (N*(N-1)*(8*())%dekai()
# print(ans)
# D


# def cal(N):
#   left = N - 3
#   right = n
#   if left < 6:
#     return 1
#   else:
#     return 1 + cal(left)

#   if right < 6:
#     return 1
#   else:
#     return 1 + cal(right)
    
    
# S = int(input())

# if S < 3:
#   print(0)
#   exit()
# else:
#   ans = cal(S)
#   print((1+ans)%dekai())




# temp = (1 + kaizyo(577))%((10**9)+7)
# print(temp)

# N = int(input())
# X_Y = [list(map(int,input().split())) for _ in range(N)]

# X が0,9以外
# nP2 * 8
# X が 0
# N = int(input())
# mod = 10**9+7
# ans = pow(10,N,mod) + pow(8,N,mod) - pow(9,N,mod) - pow(9,N,mod)
# print(ans%mod)

# D
mod = pow(10,9) + 7
S = int(input())

dp = [0] * (S+1)

dp[0] = 1

for i in range(S+1):
  for j in range(0,(i-3)+1):
    dp[i] += dp[j]
    dp[i] %= mod

print(dp[-1] % mod)