# # C


# H, W, K = map(int, input().split())
# C = [list(input()) for _ in range(H)]
# ans = 0
# # ビット探索
# for i in range(2**H):
#     for j in range(2**W):
#         cnt = 0
#         for h in range(H):
#             for w in range(W):
#                 if((i >> h) & 1) == 0 and ((j >> w) & 1) == 0:
#                     if C[h][w] == "#":
#                         cnt += 1
#         if cnt == K:
#             ans += 1

# print(ans)

# D

# N = int(input())
# A = sorted(list(map(int, input().split())), reverse=True)

# ans = 0
# cnt = 1
# # 最大値は一回だけ
# ans += A[0]

# # N-2個は、2,2,3,3,..i,i,...のように取る
# flag = False
# for i in range(1, len(A)-1):
#     ans += A[cnt]
#     if flag == False:
#         flag = True
#     else:
#         flag = False
#         cnt += 1
# print(ans)
