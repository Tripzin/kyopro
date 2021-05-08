N,A,B = map(int,input().split())
print(N-A+B)

# import math
# N = int(input())
# X = list(map(int,input().split()))
# print(sum([abs(i) for i in X]))
# print(math.sqrt(sum([abs(i)**2 for i in X])))
# xa = 0
# for x in X:
#   if abs(x) > xa:
#     xa = abs(x)
# print(xa)

# TODO: 復習すること
# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]

# N = int(input())
# nums = make_divisors(N)
# for num in nums:
#   print(num)

# from collections import deque
# X,Y,A,B = map(int,input().split())
# cnt = 0
# while X*A <= X + B and X*A < Y:
#   X *= A
#   cnt += 1

# print(cnt + (Y-1-X)//B)

# q = deque()
# q.append(X)
# max_exp = 0


# while q:

#   # print(q)
#   temp_x = q.popleft()

#   # Aのジム
#   g_a_temp_x = temp_x * A

#   # Yより小さい場合
#   if g_a_temp_x < Y:
#     q.append(g_a_temp_x)
#     max_exp += 1
#     continue

#   # Bのジム
#   g_b_temp_x = temp_x + B
#     # Yより小さい場合
#   if g_b_temp_x < Y:
#     q.append(g_b_temp_x)
#     max_exp += 1

# print(max_exp)

