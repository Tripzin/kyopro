# N = int(input())
# T,A = map(int,input().split())
# H = list(map(int,input().split()))


# ans = -1
# diff = float('inf')
# for i in range(N):
#     d = abs(1000*T-6*H[i]-1000*A)

#     if d < diff:
#         diff = d
#         ans = i + 1
# print(ans)

A,B,C,K = map(int,input().split())
ans = (B - A) * (-1 if K % 2 == 0 else 1)
if ans > 10 ** 18:
    print("Unfair")
else:
    print(ans)