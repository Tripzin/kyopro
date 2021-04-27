# import math
# N, X, T = map(int, input().split())
# print(math.ceil(N/X)*T)

# N = sum(map(int, list(input())))
# print("Yes") if N % 9 == 0 else print("No")

# N = int(input())

# print("Yes") if N % 9 == 0 else print("No")

# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for i in range(len(A)-1):
#     a_before = A[i]
#     a_after = A[i+1]

#     # print(a_before, a_after)
#     diff = a_before-a_after
#     # print(diff)
#     if diff > 0:
#         A[i+1] = a_before
#         ans += diff

# print(ans)


# from collections import deque
# # 縦(H)x横(W)
# H, W = map(int, input().split())
# # 魔法使いの座標
# CH, CW = map(int, input().split())
# # ゴール
# DH, DW = map(int, input().split())
# # マップ
# S = [list(input()) for _ in range(H)]
# # 移動Aの動き方
# move_a = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# # 移動Bの動き方
# move_b = [(x, y) for x in range(-2, 3)
#           for y in range(-2, 3) if (x, y) not in move_a + [(0, 0)]]

# INF = 10 ** 10
# # 各マスへの移動コスト
# path = [[INF] * W for _ in range(H)]

# q = deque()
# path[CH-1][CW-1] = 0
# q.append((CH-1, CW-1, 0))

# while q:

#     x, y, s = q.popleft()

#     # 移動Aについて
#     for dx, dy in move_a:
#         nx = x + dx
#         ny = y + dy

#         if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == "." and path[nx][ny] > s:
#             path[nx][ny] = s
#             q.appendleft((nx, ny, s))

# # 移動Bについて
#     for dx, dy in move_b:
#         nx = x + dx
#         ny = y + dy

#         if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == "." and path[nx][ny] > s+1:
#             path[nx][ny] = s+1
#             q.append((nx, ny, s+1))


# print(path[DH-1][DW-1]) if path[DH-1][DW-1] < INF else print(-1)


H, W, M = map(int, input().split())
boms = [tuple(map(int, input().split())) for _ in range(M)]
# boms = [list(map(int, input().split())) for _ in range(M)]

hBom = [0]*H
wBom = [0]*W

# 各行、各列の爆破対象をカウント
for h, w in boms:
    hBom[h-1] += 1
    wBom[w-1] += 1

# 爆破対象の最大数と最大になる行と列の番号を調べる
maxHBom = max(hBom)
maxWBom = max(wBom)
maxHBomIndex = [index for index, h in enumerate(hBom) if h == maxHBom]
maxWBomIndex = [index for index, w in enumerate(wBom) if w == maxWBom]

# 爆破対象が最大になる行と列の組み合わせについて、
# 爆弾を配置する場所が爆破対象であるかないかで場合分け
boms = set(boms)
for h in maxHBomIndex:
    for w in maxWBomIndex:
        if (h+1, w+1) not in boms:
            print(maxHBom + maxWBom)
            exit()
else:
    print(maxHBom + maxWBom - 1)
