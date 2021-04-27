N = int(input())
t = [int(input()) for n in range(N)]
costs = []


for i in range(1 << N):
    l_min = 0
    l_max = 0
    for j in range(N):
        if i & (1 << j):
            l_min += t[j]
        else:
            l_max += t[j]
    
    costs.append(max(l_max,l_min))

print(min(costs))
