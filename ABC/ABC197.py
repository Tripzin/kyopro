# A
# S = list(input())
# print(S[1] + S[2] +S[0])
# B
# H,W,X,Y = map(int,input().split())
# S = [list(input()) for _ in range(H)]
# cnt = 1
# H -= 1
# W -= 1
# X -= 1
# Y -= 1
# # Y軸マイナス方向
# for j in range(Y-1,-1,-1):
#   if S[X][j] == "#":
#     break
#   else:
#     # print("j={0}, X={1}".format(j,X))
#     cnt += 1
# # Y軸プラス方向
# # print("Y軸マイナス終了")
# for j in range(Y+1,W+1):
#   if S[X][j] == "#":
#     break
#   else:
#     # print("j={0}, X={1}".format(j,X))
#     cnt += 1
# # print("Y軸プラス終了")
# # X軸マイナス方向
# for i in range(X-1,-1,-1):
#   if S[i][Y] == "#":
#     break
#   else:
#     cnt += 1
# # print(cnt)
# # print("X軸マイナス終了")

# # X軸プラス方向
# for i in range(X+1,H+1):
#   if S[i][Y] == "#":
#     break
#   else:
#     cnt += 1
#     # print("i={0}, Y={1}".format(i,Y))
# # print("X軸プラス終了")
# print(cnt)

# C

# N = int(input())
# A = list(map(int,input().split()))
# if 1 == N:
#   print(A[0])
# else:
#   Ad = sorted(A)
#   print(abs(Ad[N-1]-Ad[N-2]))

# D
import math
N = int(input())
x_0,y_0 = list(map(int,input().split()))
x_2,y_2 = list(map(int,input().split()))

def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

theta = math.radians((180 * (N-2)) / N)
sin = math.sin(theta)
cos = math.cos(theta)

x_1 = (x_0 - x_2) * cos - (y_0 - y_2) * sin + x_2
y_1 = (x_0 - x_2) * sin + (y_0 - y_2) * cos + y_2

# 直径
distance = get_distance(x_0,y_0,x_2,y_2)

print(x_1*distance*math.sin(math.pi/N),y_1*distance*math.sin(math.pi/N))