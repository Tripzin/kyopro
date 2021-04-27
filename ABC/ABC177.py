# D, T, S = map(int, input().split())
# print("Yes") if D <= T * S else print("No")

# S = list(input())
# T = list(input())


# def count_diff(s_bubun, t_all):
#     cnt = 0
#     for i in range(len(s_bubun)):
#         if s_bubun[i] != t_all[i]:
#             cnt += 1
#     return cnt


# i = 0
# len_t = len(T)
# ans = 10**10
# while i+len_t <= len(S):
#     s_bubun = S[i:i+len_t]
#     kouho = count_diff(s_bubun, T)
#     ans = min(kouho, ans)
#     i += 1

# print(ans) if ans != 10**10 else print(0)


# N = int(input())
# A = list(map(int, input().split()))


# def mod10_9_7(num):
#     return num % (10**9+7)


# seki = A[-1]

# ans = 0
# for i in range(N-2, -1, -1):
#     ans += A[i] * seki
#     seki += A[i]
# print(mod10_9_7(ans))


class UnionFind():

    def __init__(self, n):
        # n個の要素
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        要素xのrootを見つける
        """
        if self.parents[x] < 0:
            return x
        else:
            # 再帰的にrootを求める
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        """
        要素x,要素yについて
        rootが同じ場合そのまま
        異なる場合は要素xの末尾に要素yを付ける
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        要素xの集合の大きさを返す
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        要素xと要素yのrootが同じか返す
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


# N人でM個の情報
N, M = map(int, input().split())
# AとBは友達であるという情報がM個
A_B = [list(map(int, input().split())) for _ in range(M)]
union = UnionFind(N)

for a, b in A_B:
    union.unite(a-1, b-1)
ans = 0
for i in range(N):
    ans = max(ans, union.size(i))
print(ans)
