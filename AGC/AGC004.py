# A
import math
A_B_C = list(map(int,input().split()))

if A_B_C[0] % 2 == 0 or A_B_C[1] % 2 == 0 or A_B_C[2] % 2 == 0:
  print(0)
else:
  max_v = max(A_B_C)
  max_i = A_B_C.index(max_v)
  ans = 1
  for i in range(len(A_B_C)):
    if max_i == i:
      ans *= (math.ceil(max_v/2) - math.floor(max_v/2))
    else:
      ans *= A_B_C[i]
    
  print(ans)



