# X = int(input())

# if 400 <= X < 600:
#     print('8')
# elif 600 <= X < 800:
#     print('7')
# elif 800 <= X <1000:
#     print('6')
# elif 1000 <= X < 1200:
#     print('5')
# elif 1200 <= X < 1400:
#     print('4')
# elif 1400 <= X < 1600:
#     print('3')
# elif 1600 <= X < 1800:
#     print('2')
# else:
#     print('1')

# A,B,C = map(int,input().split(' '))
# K = int(input())

# for k in range(K):
#     b = K - k
#     g = k

#     if A < B * 2 ** g < C * 2 ** b:
#         print("Yes")
#         exit()
# else:
#     print("No")

# N,K = map(int,input().split(' '))
# A = list(map(int,input().split(' ')))
# cnt = 0
# for k in range(K,N):
#     if A[k] > A[cnt]:
#         print("Yes")
#     else:
#         print("No")
#     cnt += 1

# S = list(input())
# w = {}
# for s in S:
#     if w.get(s) == None:
#         w[s] = 1
#     else:
#         w[s] += 1

# if len(w) == 2 and sum(w.values()) == 4:
#     print("Yes")
# else:
#     print("No")

A, B, C = map(int, input().split())
ans = C-(A-B)
print(ans) if ans > 0 else print(0)
