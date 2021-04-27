# C
X,N = map(int,input().split())
P = sorted(list(set(list(map(int,input().split())))))

cnt = 0
while True:
  if X - cnt not in P:
    print(X-cnt)
    break
  if X + cnt not in P:
    print(X+cnt)
    break
  cnt += 1



  