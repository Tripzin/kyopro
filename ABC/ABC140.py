
# C

N = int(input())
B = [10**10] + list(map(int,input().split())) + [10**10]
ans = 0
for i in range(N):
  ans += min(B[i],B[i+1])
print(ans)

# D
# import string
# N = int(input())
# strings = string.ascii_lowercase
# ans = ""

# index = 26
# cnt = 1
# # Nがcnt文字で表される場合、cnt-1文字までの場合の数を引く.
# while N > index:
#     N -= index
#     index *= 26
#     cnt += 1

# N -= 1
# for _ in range(cnt):
#     M = N % 26
#     ans += strings[M]
#     N //= 26


# # print(ans[::-1].rjust(cnt,'a'))
# print(ans[::-1].rjust(cnt,'a'))