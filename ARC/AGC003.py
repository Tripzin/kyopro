# A
from collections import Counter
S = list(input())
count = Counter(S)
flag = True

if count['N'] > 0:
  if count['S'] == 0:
    flag = False
if count['S'] > 0:
  if count['N'] == 0:
    flag = False
if count['E'] > 0:
  if count['W'] == 0:
    flag = False
if count['W'] > 0:
  if count['E'] == 0:
    flag = False
print("Yes") if flag == True else print("No")