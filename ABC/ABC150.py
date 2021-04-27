# C
import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
num = [i+1 for i in range(N)]

p_ord = 0
q_ord = 0
cnt = 0
for pre in itertools.permutations(num, N):
    if P == list(pre):
        p_ord = cnt

    if Q == list(pre):
        q_ord = cnt
    cnt += 1

print(abs(p_ord-q_ord))
