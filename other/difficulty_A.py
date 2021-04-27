# a = int(input())
# s = input()
# print(s) if a >= 3200 else print("red")

# S = list(input())
# T = list(input())

# cnt = 0
# for s, t in zip(S, T):
#     if s == t:
#         cnt += 1
# print(cnt)

# print(int(input())**3)
# weather = ["Sunny",  "Rainy", "Cloudy"]

# print(weather[weather.index(input())-1])

# import math
# N = int(input())
# mol = math.ceil(N/2) if N % 2 != 0 else N//2
# print(mol/N)
# A, B = map(int, input().split())
# print(A*B) if A <= 9 and B <= 9 else print('-1')
# w = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# w.reverse()
# print(w.index(input())+1)

# import string
# alphabet = string.ascii_lowercase
# print(alphabet[alphabet.index(input())+1])

# import math
# H, A = map(int, input().split())
# print(math.ceil(H/A))

# S, T = input().split()
# A, B = map(int, input().split())
# U = input()
# if U == S:
#     A -= 1
# else:
#     B -= 1
# print(A, B)

# S = input().split()
# for i in range(-1, 2):
#     if S[i-1] == S[i] and S[i] != S[i+1]:
#         print("Yes")
#         exit()
# else:
#     print("No")

# import math
# print(math.ceil(int(input())/2))

# print("No") if len(set(input())) == 1 else print("Yes")

# N, M = map(int, input().split())
# l = ['e'] * N + ['o'] * M
# cnt = 0
# for i in range(len(l)-1):
#     for j in range(i+1, len(l)):
#         if l[i] != l[j]:
#             pass
#         else:
#             cnt += 1
# print(cnt)


# S = list(input())

# print("Yes") if S[2] == S[3] and S[4] == S[5] else print(
#     "No")


# X, Y, Z = map(int, input().split())
# print(Z, X, Y)

# N = input()

# for n in N:
#     if n == "7":
#         print("Yes")
#         break
# else:
#     print("No")

# import math
# R = int(input())
# print(2*math.pi*R)

# S, W = map(int, input().split())

# print("unsafe") if W >= S else print("safe")

# import math
# K = int(input())
# A, B = map(int, input().split())
# largest = math.floor(B/K)*K
# print("OK") if largest >= A else print("NG")

# S = input()
# T = input()
# print("Yes") if S == T[:-1] else print("No")

# N = input()[-1]

# if N == "3":
#     print("bon")
# elif N in {"2", "4", "5", "7", "9"}:
#     print("hon")
# else:
#     print("pon")

# print("A") if input().isupper() else print("a")
