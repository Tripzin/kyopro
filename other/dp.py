# 2012 pasta
N, K = map(int, input().split())
day_pasta = {}
for _ in range(K):
    day, pasta = input().split()
    day_pasta[day] = int(pasta)

# N日分のパスタ 各日において作れるなら1作れないなら0とする.
dp = [([0]*3) for _ in range(N)]


print(dp)
# print(day_pasta)
# for n in range(1, N+1):
#     n = str(n)
#     if day_pasta.get(n):
