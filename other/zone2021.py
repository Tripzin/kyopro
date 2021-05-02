# A
# S = input()
# cnt = 0
# for i in range(len(S)-3):
#   if S[i:i+4] == "ZONe":
#     cnt += 1
# print(cnt)
# import math
# # B
# N,D,H = list(map(int,input().split()))
# d_h = [list(map(int,input().split())) for _ in range(N)]

# ans = -math.inf

# for d,h in d_h:
#   b = h - ((H-h)/(D-d))*d
#   ans = max(ans,b)
# ans = max(0,ans)
# print(ans)

# C
N = int(input())
status = [list(map(int,input().split())) for _ in range(N)]
print(status)