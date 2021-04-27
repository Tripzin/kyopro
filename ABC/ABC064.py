# C

N = int(input())
A = list(map(int,input().split()))
colors = [0] * 8
other = 0
for a in A:
  index = a // 400
  if index > 7:
    other += 1
  else:
    colors[index] += 1
min_color = 0
max_color = 0
# 全員3200以上の場合
if other == N:
  min_color = 1
  max_color = other
else:
  for c in colors:
    if c != 0:
      min_color += 1
  max_color = min_color + other 

print(min_color,max_color)
 