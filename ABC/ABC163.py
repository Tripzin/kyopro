# C
N = int(input())
A = list(map(int,input().split()))
employees = [0]*N
for a in A:
  employees[a-1] += 1
for employee in employees:
  print(employee)


