# B

N = int(input())
A = list(map(int,input().split()))

pears = {}
for index,a in enumerate(A):
  pears[index+1] = a


cnt = 0
for key,value in pears.items():
  if key == pears.get(pears.get(key)):
    cnt += 1
print(cnt//2)
