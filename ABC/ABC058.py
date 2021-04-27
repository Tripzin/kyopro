O = list(input())
E = list(input())
ans = ""

for i in range(len(O)+len(E)):
    if i % 2:
        ans += E.pop(0)
    else:
        ans += O.pop(0)

print(ans)