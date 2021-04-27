# A

N, x = map(int, input().split())
A = list(map(int, input().split()))
sum_A = sum(A)

if sum_A == x:
    print(N)
elif sum_A < x:
    print(N-1)
else:
    A = sorted(A)
    cnt = 0
    for a in A:
        x -= a
        if x >= 0:
            cnt += 1
        else:
            print(cnt)
            break
