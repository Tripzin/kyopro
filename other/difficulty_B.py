# N = int(input())
# hh = 0
# mm = 0
# # 入浴時間
# ss = 0

# hh = N//3600
# N %= 3600


# mm = N // 60
# N %= 60
# ss = N

# print("{0}:{1}:{2}".format(str(hh).zfill(2), str(mm).zfill(2), str(ss).zfill(2)))
# a = int(input())
# b = int(input())
# ans = abs(a-b) if 10-abs((a-b)) > abs(a-b) else 10-abs((a-b))
# print(ans)

# TODO: 復習　ビット探索！
# n, X = map(int, input().split())
# a = list(map(int, input().split()))

# price_sum = 0
# for i in range(n):
#     if((X >> i) & 1):
#         price_sum += a[i]
# print(price_sum)

# ABC015

# import math
# N = int(input())
# a = [bug for bug in map(int, input().split()) if bug != 0]
# print(math.ceil(sum(a)/len(a)))

# ABC016

# A, B, C = map(int, input().split())
# if A+B == C and A-B != C:
#     print("+")
# elif A+B != C and A-B == C:
#     print("-")
# elif A+B == C and A-B == C:
#     print("?")
# else:
#     print("!")

# ABC017
# X = list(input())
# flag = False
# for i in range(len(X)):
#     if X[i] not in ["o", "k", "u", "c", "h"]:
#         flag = False
#         break
#     else:
#       # chの判定
#         if i+1 < len(X) and X[i] == "c" and X[i+1] == "h":
#             flag = True
#         elif i-1 >= 0 and X[i] == "h" and X[i-1] == "c":
#             flag = True
#         elif X[i] in ["o", "k", "u"]:
#             flag = True
#         else:
#             flag = False
#             break

# print("YES") if flag else print("NO")

# ABC018

# import math

# # 文字列から左端をl,右端をrとした部分文字列を選び逆順にする
# def swap_chars(string, l, r):
#     iterate = math.ceil((r-l)/2)
#     string = list(string)
#     for i in range(iterate):
#         string[r-1], string[l-1] = string[l-1], string[r-1]
#         l += 1
#         r -= 1
#     return "".join(string)


# S = input()
# N = int(input())
# lrs = [list(map(int, input().split())) for _ in range(N)]


# for l, r in lrs:
#     S = swap_chars(S, l, r)
# print(S)

# ABC192


# def split_string(S):
#     index = 0
#     splitted_string = [S[0]]

#     for i in range(len(S)-1):
#         if S[i] == S[i+1]:
#             splitted_string[index] += S[i+1]
#         else:
#             index += 1
#             splitted_string.append(S[i+1])
#     return splitted_string


# S = input()
# ans = ""
# for s in split_string(S):
#     ans += s[0] + str(s.count(s[0]))
# print(ans)


# ABC020

# A, B = input().split()
# print(int(A+B)*2)

# ABC021

# # 街数
# N = int(input())
# # a:高橋くんが出発した街 b:自分が出発した街
# a, b = map(int, input().split())
# # たかし君が経由した街の数
# K = int(input())
# # 高橋くんが経由した街の番号(順番通りに格納されている)
# P = list(map(int, input().split()))


# if (len(set(P)) != K) or a in P or b in P:
#     print("NO")
# else:
#     print("YES")


# ABC022
# N = int(input())
# A = [int(input()) for _ in range(N)]
# zyuhun = {}

# for a in A:
#     if zyuhun.get(a):
#         zyuhun[a] += 1
#     else:
#         zyuhun[a] = 1

# cnt = 0
# for value in zyuhun.values():
#     cnt += value - 1
# print(cnt)


# ABC023
# b -> abc -> cabca -> bcabcab -> (bca)*m b (cab)*m


# def make_neckless(N):
#     neckless = "b"
#     neckless_size = 1
#     num = 0

#     while N > neckless_size:
#         judge = neckless_size % 3

#         if judge == 1:
#             neckless = "a" + neckless + "c"

#         elif judge == 2:
#             neckless = "b" + neckless + "b"

#         elif judge == 0:
#             neckless = "c" + neckless + "a"

#         neckless_size += 2
#         num += 1

#     return neckless, num


# # 入力
# N = int(input())
# S = input()

# # 手順に従った場合のサイズNのネックレスと、手順数
# neckless, number = make_neckless(N)

# # 形が同じ場合手順数を出力、異なる場合は-１を出力
# print(-1) if S != neckless else print(number)


# ABC024
# N, T = map(int, input().split())
# A = [int(input()) for _ in range(N)]
# close_time = 0
# ans = 0
# for i in range(len(A)-1):
#     close_time = A[i] + T
#     # 閉じる前に客が来たら延長
#     if close_time > A[i+1]:
#         ans += A[i+1]-A[i]
#     else:
#         ans += T

# # 最後に通った客の分を追加
# ans += T

# print(ans)


# ABC025

# def get_ans_source(distance):
#     if distance < 0:
#         return "West"
#     else:
#         return "East"


# N, A, B = map(int, input().split())

# source_and_distance = [input().split() for _ in range(N)]
# ans_distance = 0

# for source, distance in source_and_distance:
#     move = 0
#     if int(distance) < A:
#         move = A
#     elif int(distance) > B:
#         move = B
#     else:
#         move = int(distance)

#     # 東ならプラス、西ならマイナス
#     if source == "East":
#         ans_distance += move
#     else:
#         ans_distance -= move

# if ans_distance == 0:
#     print(0)
# else:
#     ans_source = get_ans_source(ans_distance)
#     print("{0} {1}".format(ans_source, abs(ans_distance)))

# ABC026
# import math
# N = int(input())
# R = sorted([int(input()) for _ in range(N)], reverse=True)
# ans = 0
# white = False
# for r in R:
#     if white:
#         ans -= math.pow(r, 2)
#     else:
#         ans += math.pow(r, 2)
#     white = not white
# print(ans*math.pi)

# # ABC027
# import math


# def average(residents, N):
#     ceil = math.ceil(sum(residents)/N)
#     floor = math.floor(sum(residents)/N)
#     if ceil != floor:
#         return -1
#     else:
#         return sum(residents)//N


# N = int(input())
# A = list(map(int, input().split()))
# residents_average = average(A, N)

# if residents_average == -1:
#     print(-1)
#     exit()


# cnt = 0
# left = 0
# for i in range(N-1):
#     left += A[i]
#     if left != residents_average * (i+1):
#         cnt += 1

# print(cnt)

# ABC028

# def counts(S):
#     ans = [0]*6
#     cnt = 0
#     for s in ('A', 'B', 'C', 'D', 'E', 'F'):
#         ans[cnt] = str(S.count(s))
#         cnt += 1
#     return ans


# S = input()
# print(" ".join(counts(S)))

# # ABC029
# cnt = 0
# for _ in range(12):
#     if input().count("r") > 0:
#         cnt += 1
# print(cnt)

# ABC030

# def time24_to_time12(time24):
#     if time24 > 12:
#         return time24 - 12
#     else:
#         return time24


# def degree_hour(hour, minute):
#     return (hour*60+minute)*0.5


# def degree_minute(minute):
#     return minute*6


# n, m = map(int, input().split())

# time12 = time24_to_time12(n)

# hour_arg = degree_hour(time12, m)
# min_arg = degree_minute(m)

# ans = abs(hour_arg - min_arg)

# if ans < 360:
#     print(min(ans, 360-ans))
# else:
#     print(ans - 360)

# ABC031
# L, H = map(int, input().split())
# N = int(input())
# A = [int(input()) for _ in range(N)]

# for a in A:
#     # 過足の場合
#     if a > H:
#         print(-1)
#     # 不足の場合
#     elif a < L:
#         print(L-a)
#     else:
#         print(0)

# ABC032
# s = input()
# k = int(input())

# a = set()

# for i in range((len(s))-k+1):
#     if s[i:i+k] not in a:
#         a.add(s[i:i+k])
# print(len(a))
# ABC033
# N = int(input())
# ans_name = ""
# sum_people = 0
# max_people = 0

# for _ in range(N):
#     name, people = input().split()
#     people = int(people)
#     sum_people += people
#     if people > max_people:
#         max_people = people
#         ans_name = name

# print(ans_name) if max_people > sum_people/2 else print("atcoder")

# ABC034

# n = int(input())
# print(n+1) if n % 2 else print(n-1)

# ABC035
# def manhattan_distance(x_y):
#     return abs(x_y[0]) + abs(x_y[1])


# def move(s, x_y):
#     if s == "L":
#         return (x_y[0]-1, x_y[1])
#     elif s == "U":
#         return (x_y[0], x_y[1]+1)
#     elif s == "R":
#         return (x_y[0]+1, x_y[1])
#     elif s == "D":
#         return (x_y[0], x_y[1]-1)


# def move_min_max(T, x_y):
#     ans_x_y = x_y
#     if T == 1:
#         distance_moved_x_y = -10 ** 10
#     elif T == 2:
#         distance_moved_x_y = 10 ** 10

#     for nx, ny in [(0, -1), (1, 0), (0, 1), (0, -1)]:

#         moved_x_y = (x_y[0]+nx, x_y[1]+ny)
#         temp_distance = manhattan_distance(moved_x_y)

#         # 最大値を探す
#         if T == 1:
#             if temp_distance > distance_moved_x_y:
#                 ans_x_y = moved_x_y
#                 distance_moved_x_y = temp_distance
#         # 最小値を探す
#         elif T == 2:
#             if temp_distance < distance_moved_x_y:
#                 ans_x_y = moved_x_y
#                 distance_moved_x_y = temp_distance

#     return ans_x_y

# from collections import Counter
# S = input()
# T = int(input())

# c = Counter(S)
# d = abs(c['U']-c['D']) + abs(c['R']-c['L'])

# if T == 1:
#     ans = d + c['?']
# else:
#     if d - c['?'] >= 0:
#         ans = d - c['?']
#     else:
#         ans = (c['?'] - d) % 2
# print(ans)

# ABC036
# N = int(input())
# S = [list(input()) for _ in range(N)]
# for j in range(N):
#     for i in range(N-1, -1, -1):
#         print(S[i][j], end="")
#     print("")

# ABC037
# def rewrite(a, l, r, t):
#     """
#     配列aのl番目からr番目をtに置き換える
#     """
#     for i in range(l-1, r):
#         a[i] = t
#     return a


# def print_ans(A):
#     for a in A:
#         print(a)


# N, Q = map(int, input().split())
# # L_i番目からR_i番目をT_iに置き換える
# L_R_T = [list(map(int, input().split())) for _ in range(Q)]
# a = [0] * N

# for l, r, t in L_R_T:
#     a = rewrite(a, l, r, t)
# print_ans(a)

# # ABC038

# H_1, W_1 = map(int, input().split())
# H_2, W_2 = map(int, input().split())


# if H_1 in (H_2, W_2) or W_1 in (H_2, W_2):
#     print("YES")
# else:
#     print("NO")

# ABC039
# import math
# X = int(input())
# print(int(math.sqrt(math.sqrt(X))))

# ABC040
# NICE:diffculty 595
# import math
# n = int(input())
# abs_diff = 10**10
# amari = 10**10
# ans = abs_diff + amari
# chukan = math.floor(math.sqrt(n))
# # print(chukan)
# for h in range(1, chukan+1):
#     w = math.floor(n/h)
#     # print(h, w)
#     abs_diff = abs(h-w)
#     amari = n - h*w
#     ans = min(ans, abs_diff+amari)
# print(ans)

# # ABC041
# def mod10_9_7(num):
#     return num % (10**9+7)


# A, B, C = map(int, input().split())

# print(mod10_9_7(A*B*C))

# # ABC042
# N, L = map(int, input().split())
# S = sorted([input() for _ in range(N)])
# print("".join(S))

# ABC043

# from collections import deque
# S = input()
# q = deque()

# for s in S:
#     if s == "B":
#         if len(q) != 0:
#             q.pop()
#     else:
#         q.append(s)
# print("".join(q))

# ABC044
# from collections import Counter

# w = input()

# countAlphabets = Counter(w)
# for count in countAlphabets.values():
#     if count % 2 != 0:
#         print("No")
#         exit()

# print("Yes")

# # ABC045
# from collections import deque
# S_A = deque(input())
# S_B = deque(input())
# S_C = deque(input())

# # 最初はAから
# next_turn = 'a'

# while True:
#     # 勝利判定
#     if len(S_A) == 0 and next_turn == 'a':
#         print("A")
#         exit()
#     elif len(S_B) == 0 and next_turn == 'b':
#         print("B")
#         exit()
#     elif len(S_C) == 0 and next_turn == 'c':
#         print("C")
#         exit()
#     else:
#         if next_turn == 'a':
#             next_turn = S_A.popleft()
#         elif next_turn == 'b':
#             next_turn = S_B.popleft()
#         elif next_turn == 'c':
#             next_turn = S_C.popleft()

# ABC046
# N, K = map(int, input().split())
# print(K*(K-1)**(N-1))

# ABC047
# W, H, N = map(int, input().split())
# X_Y_A = [map(int, input().split()) for _ in range(N)]
# oX = 0
# oY = 0
# for x, y, a in X_Y_A:
#     if a == 1:
#         oX = max(x, oX)
#     elif a == 2:
#         W = min(x, W)
#     elif a == 3:
#         oY = max(y, oY)
#     else:
#         H = min(y, H)

# 両方マイナスのとき+になってWA
# A = (W-oX)*(H-oY)
# print(A) if A > 0 else print(0)
# print(W, oX, H, oY)
# print(max(0, W-oX)*max(0, H-oY))
# import math


# def ceil(bunshi, bunbo):
#     if bunshi > 10 ** 10:
#         return math.ceil(((bunshi/(10**10))/(bunbo))*(10**10))
#     else:
#         return math.ceil(bunshi/bunbo)


# def floor(bunshi, bunbo):
#     if bunshi > 10 ** 10:
#         return math.floor(((bunshi/(10**10))/(bunbo))*(10**10))
#     else:
#         return math.floor(bunshi/bunbo)


# # ABC048
# a, b, x = map(int, input().split())

# print(b//x - a//x + (a % x == 0))

# ABC052

# N = int(input())
# S = input()
# x = 0
# ans = 0
# for s in S:
#     if s == "I":
#         x += 1
#     else:
#         x -= 1
#     ans = max(ans, x)
# print(ans)

# ABC053
# S = input()
# a_index = 10**10
# z_index = -1
# for i in range(len(S)):
#     if S[i] == "A":
#         a_index = min(a_index, i)
#     if S[i] == "Z":
#         z_index = max(z_index, i)
# print(z_index-a_index+1)

# ABC054
# import math
# N, M = map(int, input().split())
# A = [list(input()) for _ in range(N)]
# B = [list(input()) for _ in range(M)]

# for i in range(0, math.ceil(N/M)):
#     for j in range(0, math.ceil(N/M)):
#         # 畳み込み
#         flag = True
#         for l in range(0, M):
#             for m in range(0, M):
#                 if A[l+i][m+j] != B[l][m]:
#                     flag = False
#                     break
#         if flag == True:
#             print("Yes")
#             exit()
# print("No")

# # ABC055
# N = int(input())
# power = 1
# for n in range(1, N+1):
#     power = power % (10**9+7) * n
# print(power % (10**9+7))

# ABC056

# W, a, b = map(int, input().split())
# if b+W < a:
#     print(a-(b+W))
# elif b > a+W:
#     print(b-(a+W))
# else:
#     print(0)

# ABC057
# N, M = map(int, input().split())

# # 学生N人の現在地(a,b)
# A_B = [list(map(int, input().split())) for _ in range(N)]
# # チェックポイントM個の場所(c,d)
# C_D = [list(map(int, input().split())) for _ in range(M)]


# for a, b in A_B:
#     temp_distance = 10**10
#     temp_checkpoint = -1
#     checkpoint_count = 1
#     for c, d in C_D:
#         manhattan_distance = abs(a-c) + abs(b-d)
#         if temp_distance > manhattan_distance:
#             temp_distance = manhattan_distance
#             temp_checkpoint = checkpoint_count
#         checkpoint_count += 1
#     print(temp_checkpoint)

# ABC100

# D, N = map(int, input().split())
# print(N*100**D) if N != 100 else print((N+1)*100**D)

# ABC059

# A = int(input())
# B = int(input())
# if A > B:
#     print("GREATER")
# elif A < B:
#     print("LESS")
# else:
#     print("EQUAL")

# ABC060

# A, B, C = map(int, input().split())

# for i in range(1, B+1):
#     if i*A % B == C:
#         print("YES")
#         exit()
# print("NO")

# ABC061

# N, M = map(int, input().split())
# # 都市Aと都市Bを結ぶ路線M
# A_B = [list(map(int, input().split())) for _ in range(M)]
# ans = [0] * N

# for a, b in A_B:
#     ans[a-1] += 1
#     ans[b-1] += 1
# for a in ans:
#     print(a)

# ABC062

# H, W = map(int, input().split())
# A = [list(input()) for _ in range(H)]

# # 一段目
# print("#"*(W+2))
# for a in A:
#     print("#" + "".join(a) + "#")
# # 最終段
# print("#"*(W+2))

# # ABC063
# from collections import Counter

# S = input()
# count = Counter(S)

# for cnt in count.values():
#     if cnt != 1:
#         print('no')
#         exit()
# else:
#     print('yes')

# ABC064

# N = int(input())
# a = list(map(int, input().split()))
# print(max(a)-min(a))

# ABC065

# N = int(input())
# A = [int(input())-1 for _ in range(N)]
# cnt = 1
# next_button = 0
# while cnt <= len(A):
#     next_button = A[next_button]
#     if next_button == 1:
#         print(cnt)
#         exit()
#     cnt += 1
# print(-1)

# ABC066

# S = input()

# for i in range(1, len(S)):
#     gumozi = S[0:len(S)-i]

#     if gumozi[0:len(gumozi)//2] == gumozi[(len(gumozi)//2):len(gumozi)]:
#         print(len(gumozi))
#         exit()
# print(0)

# ABC067

# N, K = map(int, input().split())
# l = sorted(list(map(int, input().split())))
# l.reverse()
# print(sum(l[:K]))

# ABC068

# N = int(input())
# i = 0
# while True:
#     if 2**i > N:
#         print(2**(i-1))
#         exit()
#     i += 1

# # ABC069
# s = input()

# print(s[0] + str(len(s[0:-2])) + s[-1])

# ABC070

# A, B, C, D = map(int, input().split())

# print(max(0, min(B, D)-max(A, C)))

# ABC071

# import string

# all_string = set(string.ascii_lowercase)
# S = set(input())

# ans = sorted(list(all_string - S))

# print(ans[0]) if ans != [] else print("None")


# # ABC072
# S = input()
# for i in range(len(S)):
#     if i % 2 == 0:
#         print(S[i], end="")
# print()

# # ABC073
# N = int(input())
# L_R = [map(int, input().split()) for _ in range(N)]
# ans = 0
# for l, r in L_R:
#     ans += r - l + 1
# print(ans)

# # ABC074

# N = int(input())
# K = int(input())
# X = list(map(int, input().split()))

# ans = 0
# for x in X:
#     ans += min(x, K-x)*2
# print(ans)

# ABC075

# def mine_count(x, y, ans):
#     ans[y][x] = 0
#     for nx, ny in (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1):
#         if 0 <= y+ny < H and 0 <= x+nx < W:
#             if ans[y+ny][x+nx] == "#":
#                 ans[y][x] += 1
#     return ans


# H, W = map(int, input().split())
# S = [list(input()) for _ in range(H)]
# ans = S
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == ".":
#             ans = mine_count(j, i, ans)

# for row in ans:
#     for item in row:
#         print(item, end="")
#     print()

# ABC076

# N = int(input())
# K = int(input())
# ans = 1
# for i in range(N):
#     ans = min(ans*2, ans+K)
# print(ans)


# ABC077

# N = int(input())
# for i in range(1, N+1):
#     if i*i > N:
#         print((i-1)*(i-1))
#         exit()
# print(1)

# ABC078
# import math
# X, Y, Z = map(int, input().split())

# X -= Z

# print(math.floor(X/(Y+Z)))

# ABC079

# N = int(input())
# L = [2, 1] + [0] * (N-1)
# for i in range(2, N+1):
#     L[i] = L[i-1] + L[i-2]

# print(L[N])

# ABC080

# N = input()
# X = int(N)
# if X % sum(list(map(int, N))) == 0:
#     print("Yes")
# else:
#     print("No")

# ABC081
# N = int(input())
# A = list(map(int, input().split()))

# i = 1
# while True:
#     for a in A:
#         if a % (2**i) == 0:
#             pass
#         else:
#             print(i-1)
#             exit()
#     i += 1

# ABC171

# N, K = map(int, input().split())
# P = sorted(list(map(int, input().split())))

# print(sum(P[:K]))

# ABC170

# X, Y = map(int, input().split())

# for k in range(X+1):
#     t = X - k
#     if k*4 + t*2 == Y:
#         print("Yes")
#         exit()
# print("No")

# # ABC169
# N = int(input())
# A = list(map(int, input().split()))

# ans = 1
# if 0 in A:
#     print(0)
#     exit()
# for a in A:
#     ans *= a
#     if ans > 10**18:
#         print('-1')
#         exit()

# print(ans)

# # ABC168

# K = int(input())
# S = input()

# if len(S) > K:
#     print(S[:K]+"...")
# else:
#     print(S)

# ABC167

# A, B, C, K = map(int, input().split())

# ans = 0
# if A >= K:
#     print(K)
#     exit()
# else:
#     ans += A
#     K -= A
#     if B >= K:
#         print(ans)
#         exit()
#     else:
#         K -= B
#         ans -= K
#         print(ans)

# ABC166

# N, K = map(int, input().split())
# cnts = [0] * N
# for n in range(K):
#     d = int(input())
#     A = list(map(int, input().split()))

#     for a in A:
#         cnts[a-1] += 1
# cnt = 0
# for c in cnts:
#     if c == 0:
#         cnt += 1
# print(cnt)

# ABC165
# X = int(input())
# bank = 100
# cnt = 0
# while bank < X:
#     bank = bank + bank//100
#     cnt += 1
# print(cnt)

# ABC164
# import math
# A, B, C, D = map(int, input().split())
# while True:
#     C -= B
#     if C <= 0:
#         print("Yes")
#         exit()
#     A -= D
#     if A <= 0:
#         print("No")
#         exit()

# # ABC163
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# print(N-sum(A)) if N - sum(A) >= 0 else print(-1)

# ABC083
# N, A, B = map(int, input().split())
# ans = 0

# for n in range(1, N+1):
#     n_sum_digit = sum(map(int, list(str(n))))
#     if B >= n_sum_digit >= A:
#         ans += n
# print(ans)

# A, B = map(int, input().split())
# S = input()

# if len(S) != A+B+1:
#     print("No")
#     exit()

# for i in range(A+B+1):

#     if i == A:
#         if S[i] != "-":
#             print('No')
#             exit()
#     else:
#         if not('0' <= S[i] <= '9'):
#             print('No')
#             exit()
# print('Yes')


# ABC085

# N = int(input())
# D = sorted([int(input()) for _ in range(N)], reverse=True)
# cnt = 1
# for i in range(len(D)-1):
#     if D[i] <= D[i+1]:
#         pass
#     else:
#         cnt += 1
# print(cnt)

# ABC133
# import math


# def calc_distance(Y, Z):
#     temp = 0
#     for y, z in zip(Y, Z):
#         temp += (y-z)**2
#     return temp


# def is_integer(num):
#     for k in range(1, num+1):
#         if k*k == num:
#             return True
#     else:
#         return False


# N, D = map(int, input().split())
# X = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# for i in range(len(X)-1):
#     for j in range(i, len(X)):
#         distance = calc_distance(X[i], X[j])
#         if is_integer(distance):
#             cnt += 1
# print(cnt)


# ABC135

# N = int(input())
# P = list(map(int, input().split()))
# sorted_P = sorted(P)
# cnt = 0
# for i in range(len(P)):
#     if P[i] != sorted_P[i]:
#         cnt += 1

#     if cnt > 2:
#         print("NO")
#         exit()
# print("YES")

# ABC136

# N = int(input())

# if 1 <= N < 10:
#     print(N)
# elif 10 <= N < 100:
#     print(9)
# elif 100 <= N < 1000:
#     print((N-100+1)+9)
# elif 1000 <= N < 10000:
#     print(9+900)
# elif 10000 <= N < 100000:
#     print((N-10000+1)+900+9)
# else:
#     print(90000+900+9)

# ABC087

# A, B, C, X = [int(input()) for _ in range(4)]
# cnt = 0
# for a in range(0, A+1):
#     for b in range(0, B+1):
#         for c in range(0, C+1):
#             if 500*a+100*b+50*c == X:
#                 cnt += 1
# print(cnt)

# ABC088

# N = int(input())
# A = sorted(list(map(int, input().split())))
# offset = True if len(A) % 2 == 0 else False
# alice = sum(A[offset::2])
# bob = sum(A[not offset::2])
# print(alice-bob)

# ABC089
# N = int(input())
# S = set(input().split(" "))

# if len(S) == 3:
#     print("Three")
# elif len(S) == 4:
#     print("Four")

# ABC090

# A, B = map(int, input().split())
# cnt = 0
# for num in range(A, B+1):
#     num = list(str(num))
#     for i in range(len(num)//2):
#         if num[i] != num[len(num)-i-1]:
#             break
#     else:
#         cnt += 1
# print(cnt)

# ABC091
# from collections import Counter
# N = int(input())
# S = Counter([input() for _ in range(N)])
# M = int(input())
# T = Counter([input() for _ in range(M)])

# ans = 0

# for word, count in S.items():
#     temp = count - T[word]
#     ans = max(ans, temp)
# print(ans)

# # ABC092
# # 参加者
# N = int(input())
# # D日間の合宿でX個のチョコが残った
# D, X = map(int, input().split())
# # 参加者iは,1,Ai+1,2Ai+1..目にチョコを一つ食べる
# A = [int(input()) for _ in range(N)]

# eaten = 0
# for i in range(N):
#     day = 0
#     cnt = 0
#     while True:
#         day = A[i]*cnt + 1
#         if day <= D:
#             eaten += 1
#             cnt += 1
#         else:
#             break
# print(eaten+X)

# # ABC093
# A, B, K = map(int, input().split())

# for num in range(A, min(B+1, A+K)):
#     print(num)
# for num in range(max(A+K, B-K+1), B+1):
#     print(num)

# ABC094

# N, M, X = map(int, input().split())
# A = list(map(int, input().split()))


# left = 0
# right = 0

# for a in A:
#     if a > X:
#         right += 1
#     else:
#         left += 1
# print(min(left, right))

# ABC095

# N, X = map(int, input().split())
# M = [int(input()) for _ in range(N)]

# min_M = min(M)
# sum_M = sum(M)

# print(N+((X-sum_M)//min_M))

# ABC096

# nums = sorted(list(map(int, input().split())), reverse=True)
# K = int(input())

# print(nums[0]*(2**K) + nums[1] + nums[2])

# ABC097

# X = int(input())
# b = 2
# p = 2
# ans = 1
# for b in range(1, X+1):
#     for p in range(2, X+1):
#         beki = b ** p
#         if beki <= X:
#             ans = max(ans, beki)
#         else:
#             break
# print(ans)

# # ABC098

# N = int(input())
# S = input()
# ans = 0
# for i in range(len(S)):
#     left = set(S[0:i])
#     right = set(S[i:len(S)])

#     ans = max(ans, len(left & right))
# print(ans)

# ABC099
# a, b = map(int, input().split())

# for n in range(0, 1000):
#     west = ((n*(n-1))/2)-a
#     east = ((n*(n+1))/2)-b

#     if west == east:
#         print(int(east))
#         exit()

# ABC106

# N = int(input())
# ans = 0
# for n in range(1, N+1):
#     cnt = 0
#     for i in range(1, n+1):
#         if (n % i == 0) and (n % 2 == 1):
#             cnt += 1
#     if cnt == 8:
#         ans += 1
# print(ans)

# ABC107
# H, W = map(int, input().split())
# A = [list(input()) for _ in range(H)]
# # 列について
# for i in range(H):
#     for j in range(W):
#         if A[i][j] == "#":
#             break
#     # すべて空白だったらx印
#     else:
#         for l in range(W):
#             A[i][l] = "x"

# # 行について
# for i in range(W):
#     for j in range(H):
#         if A[j][i] == "#":
#             break
#     else:
#         for l in range(H):
#             A[l][i] = "x"
# for i in range(H):
#     x_cnt = 0
#     for j in range(W):
#         if A[i][j] != "x":
#             print(A[i][j], end="")
#         else:
#             x_cnt += 1

#     if x_cnt < W:
#         print()
#     else:
#         pass


# ABC146
# import string
# N = int(input())
# S = input()
# ascii_uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# for s in S:
#     s_index = ascii_uppercase.index(s)
#     ans_index = (s_index + N) % len(ascii_uppercase)
#     print(ascii_uppercase[ans_index], end="")


# ABC151

# N, K, M = map(int, input().split())
# A = list(map(int, input().split()))

# ans = N*M - sum(A)

# if K >= ans >= 0:
#     print(ans)
# elif ans < 0:
#     print(0)
# else:
#     print('-1')

# ABC150
# N = int(input())
# S = input()
# cnt = 0
# for i in range(len(S)-2):
#     if S[i:i+3] == "ABC":
#         cnt += 1
# print(cnt)

# ABC164
# S = input()
# print("x"*len(S))

# ABC155

# N = int(input())
# A = list(map(int, input().split()))

# for a in A:
#     if a % 2 == 0:
#         if a % 3 == 0 or a % 5 == 0:
#             pass
#         else:
#             print("DENIED")
#             exit()
# print("APPROVED")


# # ABC159

# def is_kaibun(string):

#     for i in range((len(string)//2)+1):
#         if string[i] != string[len(string)-i-1]:
#             return False
#     else:
#         return True


# S = input()
# if is_kaibun(S) and is_kaibun(S[0:(len(S)-1)//2]) and is_kaibun(S[((len(S)+3)//2)-1:len(S)]):
#     print("Yes")
# else:
#     print("No")

# # abc103
# S = input()
# T = input()
# temp = S
# for i in range(len(S)):
#     if temp == T:
#         print("Yes")
#         exit()
#     else:
#         temp = temp[-1] + temp[:-1]
# print("No")

# ABC145

# N = int(input())
# S = input()

# if len(S) % 2 != 0:
#     print("No")
#     exit()

# else:
#     l = len(S)
#     if S[0:l//2] == S[l//2:l]:
#         print("Yes")
#     else:
#         print("No")


# ABC109

# N = int(input())
# W = [input() for _ in range(N)]
# used = []

# first = W[0]
# used.append(first)

# for index in range(1, len(W)):
#     if W[index][0] == W[index-1][-1] and W[index] not in used:
#         used.append(W[index])
#     else:
#         print("No")
#         exit()
# print("Yes")

# ABC143

# N = int(input())
# D = list(map(int, input().split()))
# ans = 0

# for i in range(len(D)-1):
#     for j in range(i+1, len(D)):
#         ans += D[i]*D[j]
# print(ans)

# ABC110
# N, M, X, Y = map(int, input().split())
# max_X = max(list(map(int, input().split())))
# min_Y = min(list(map(int, input().split())))

# for Z in range(X+1, Y+1):
#     if max_X < Z <= min_Y:
#         print("No War")
#         exit()
# else:
#     print("War")

# ABC144

# N = int(input())
# for i in range(1, 10):
#     for j in range(1, 10):
#         if N == i*j:
#             print("Yes")
#             exit()
# print("No")

# # ABC147

# S = input()
# cnt = 0
# for i in range(len(S)//2):
#     if S[i] != S[len(S)-i-1]:
#         cnt += 1
# print(cnt)


# # ABC160

# X = int(input())

# ans = 0
# coin_500 = 0
# coin_5 = 0
# coin_500 = X//500
# X = X - coin_500*500
# coin_5 = X//5
# print(coin_500*1000+coin_5*5)

# ABC161

# N, M = map(int, input().split())
# A = list(map(int, input().split()))


# line = sum(A)/(4*M)
# cnt = 0
# for a in A:
#     if a >= line:
#         cnt += 1
# if cnt >= M:
#     print("Yes")
# else:
#     print("No")

# ABC117

# N = int(input())
# L = sorted(list(map(int, input().split())))

# max_length = L[-1]
# sum_length = sum(L[0:len(L)-1])

# print("Yes") if max_length < sum_length else print("No")

# ABC162

# N = int(input())
# ans = 0
# for n in range(1, N+1):
#     if n % 3 == 0 and n % 5 == 0:
#         pass
#     elif n % 3 == 0:
#         pass
#     elif n % 5 == 0:
#         pass
#     else:
#         ans += n % (10**9+7)
# print(ans)


# ABC101

# N = int(input())
# S_N = sum(list(map(int, list(str(N)))))
# ans = N % S_N
# print("Yes") if ans == 0 else print("No")

# ABC102

# N = int(input())
# A = list(map(int, input().split()))
# print(abs(max(A)-min(A)))

# ABC104

# S = input()
# C_cnt = 0
# if S[0] == 'A' and S[1].islower() and S[-1].islower():
#     temp = S[2:len(S)]
#     if temp.count('C') == 1:
#         for t in temp:
#             if t != "C" and t.isupper() == True:
#                 print("WA")
#                 exit()
#         else:
#             print("AC")
#             exit()
# print("WA")

# ABC105

# N = int(input())

# for i in range(25):
#     for j in range(15):
#         if i*4 + j*7 == N:
#             print("Yes")
#             exit()
# else:
#     print("No")

# # ABC108

# x_1, y_1, x_2, y_2 = map(int, input().split())

# x = x_2 - x_1
# y = y_2 - y_1

# print(x_2-y, y_2+x, x_1-y, y_1+x)

# ABC158

# N, A, B = map(int, input().split())

# X = N//(A+B)
# Y = N % (A+B)

# print(X*A+min(A, Y))

# ABC153


# H, N = map(int, input().split())
# A = sorted(list(map(int, input().split())), reverse=True)
# print("Yes") if H - sum(A) <= 0 else print("No")

# # ABC152

# a, b = map(int, input().split())
# print(min(str(a)*b, str(b)*a))

# ABC149

# A, B, K = map(int, input().split())

# print(max(0, A-K), end=" ")

# K = max(0, K-A)
# print(max(0, B-K))

# # ABC148
# N = int(input())
# S, T = input().split()

# ans = ""

# for i in range(N):
#     ans = ans + S[i] + T[i]

# print(ans)

# # ABC142

# N, K = map(int, input().split())
# H = list(map(int, input().split()))
# cnt = 0

# for h in H:
#     if h >= K:
#         cnt += 1
# print(cnt)

# ABC141

# S = input()

# for i in range(len(S)):
#     # 0オリジン[偶数]
#     if i % 2 == 0:
#         if S[i] not in ['R', 'U', 'D']:
#             print("No")
#             exit()
#     else:
#         if S[i] not in ['L', 'U', 'D']:
#             print("No")
#             exit()
# print("Yes")

# ABC140

# N = int(input())
# A = [0] + list(map(int, input().split()))
# B = [0] + list(map(int, input().split()))
# C = [0] + list(map(int, input().split()))
# ans = 0
# for i in range(1, N+1):
#     ans += B[A[i]]
#     if i > 1:
#         if A[i] == A[i-1]+1:
#             ans += C[A[i-1]]
# print(ans)

# ABC116

# def f(n):
#     if n % 2 == 0:
#         return n/2
#     else:
#         return 3*n+1


# s = int(input())
# cnt = 0
# a = [s]
# while True:

#     temp = f(a[cnt])

#     if temp in a:
#         print(len(a)+1)
#         exit()
#     a.append(temp)
#     cnt += 1

# ABC115

# N = int(input())
# P = [int(input()) for _ in range(N)]

# print(sum(P)-max(P)//2)

# ABC114

# S = list(input())
# ans = 10 * 100
# for i in range(len(S)-2):
#     num = int("".join(S[i:i+3]))
#     ans = min(abs(num-753), ans)
# print(ans)

# # ABC112

# N, T = map(int, input().split())
# C_T = [map(int, input().split()) for _ in range(N)]
# temp_c = 10**10
# for c, t in C_T:
#     if t <= T and c <= temp_c:
#         temp_c = c


# if temp_c == 10**10:
#     ans = "TLE"
# else:
#     ans = temp_c
# print(ans)

# # ABC111

# N = int(input())

# zorome_contest = [111*i for i in range(1, 10)]
# diff_min = 10**10
# ans = 0

# for contest in zorome_contest:
#     if contest - N >= 0 and contest - N < diff_min:
#         diff_min = contest - N
#         ans = contest
# print(ans)


# # ABC138

# N = int(input())
# A = list(map(int, input().split()))
# bunbo = 0

# for a in A:
#     bunbo += 1/a
# print(1/bunbo)


# ABC132

N = int(input())
P = list(map(int, input().split()))
cnt = 0
for n in range(N-2):
    if P[n] < P[n+1] < P[n+2] or P[n+2] < P[n+1] < P[n]:
        cnt += 1
print(cnt)
