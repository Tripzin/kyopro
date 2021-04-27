# A
a,b =map(int,input().split())

if 0 < a and 0 < b:
  print("Positive")
elif (a == 0 or b == 0) or (a < 0 and 0 < b):
  print("Zero")
else:
  if (a-b)%2 == 0:
    print("Negative")
  else:
    print("Positive")
