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
