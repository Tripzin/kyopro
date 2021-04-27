# S = input()
# T = input()

# if S == "Y":
#   print(T.upper())
# else:
#   print(T)

# H,W = map(int,input().split())
# S = [list(input()) for _ in range(H)]
# cnt = 0
# for i in range(H):
#   for j in range(W):
#     if (i+1) < H:

#       if S[i][j] == '.' and S[i+1][j] == '.':
#        cnt += 1


#     if (j+1) < W:
#       if S[i][j] == '.' and S[i][j+1] == '.':
#         cnt += 1
# print(cnt)




N = int(input())
P = list(map(int,input().split()))
m = 0
a = [0] * 200000
# ans(i) > ans(i+1) は起こり得ない
for p in P:
  a[p] = 1
  while a[m] == 1:
    m += 1
  print(m)


