# a,b,c = map(int,input().split())
# print(abs(7-a)+abs(7-b)+abs(7-c))

# B
# S = input()
# for s in reversed(S):
#   if s == "6":
#     print("9", end="")
#   elif s == "9":
#     print("6", end="")
#   else:
#     print(s, end="")

# C

# def counts(nums,N):
#   list_d = [[] for _ in range(N)]
#   for i in range(len(nums)):
#     list_d[nums[i]-1].append(i)
#   return list_d

# N = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# C = list(map(int,input().split()))

# count = 0

# A_d, B_d, C_d = counts(A,N), counts(B,N), counts(C,N)

# for i in range(N):
#   if len(B_d) == 0:
#     count += 0
#   else:
#     for b in B_d[i]:
#       count += len(A_d[i]) * len(C_d[b])
# print(count)

# print(A_d)
# print(B_d)
# print(C_d)

# D
A, B, K = input().split()


