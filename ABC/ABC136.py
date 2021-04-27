# C

N = int(input())
H = list(map(int,input().split()))
H.reverse()
for i in range(len(H)-1):
  if H[i] - H[i+1] == -1:
    H[i+1] -= 1
  elif H[i] - H[i+1] < -1:
    print('No')
    exit()
  
else:
  print('Yes')
