# A
S = input()
ans = 0
prev = ""
now = ""
for s in S:
  now += s
  if now != prev:
    ans += 1
    prev = now
    now = ""
print(ans)
