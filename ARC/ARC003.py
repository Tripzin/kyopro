from collections import Counter

N = int(input())
R = list(input())

count = Counter(R)

ans = 0

for key,value in count.items():
  if key == "A":
    ans += 4 * value
  elif key == "B":
    ans += 3 * value
  elif key == "C":
    ans += 2 * value
  elif key == "D":
    ans += value
print(ans/len(R))




