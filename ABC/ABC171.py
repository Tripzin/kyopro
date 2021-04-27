# # D
# from collections import Counter
# N = int(input())
# # 正数列A
# A = list(map(int, input().split()))
# Q = int(input())
# # B_iである要素をC_iに置き換える
# B_C = [list(map(int, input().split())) for _ in range(Q)]

# all_count = Counter(A)
# S = sum(A)

# for B, C in B_C:

#     count_B = all_count[B]
#     all_count[B] = 0
#     all_count[C] += count_B
#     S = S + (C-B)*count_B

#     print(S)

# E
"""
N=4のとき
A1,A2,A3,A4をわかっているxorの値、
スカーフに書かれた数をX1,X2,X3,X4とすると
X2^X3^X4 = A1,
X1^X3^X4 = A2,
X1^X2^X4 = A3,
X1^X2^X3 = A4
である
ごにょごにょすると
X1 = (A1^A2^A3^A4)^A4
...
X4 = (A1^A2^A3^A4)^A1
であるとわかる
"""
N = int(input())
A = list(map(int, input().split()))
all_xor = 0
for a in A:
    all_xor ^= a

for i in range(N):
    ans = all_xor ^ A[i]
    print(ans, end=" ")
print()
