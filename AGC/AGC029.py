# A
S = input()
cnt = 0
B_cnt = 0
ans = 0
for s in reversed(S):
    # print(s)
    if s == "B":
        ans += (cnt - B_cnt)
        B_cnt += 1
    cnt += 1
    # print("B_cnt: " + str(B_cnt))
    # print("Cnt:" + str(cnt))
print(ans)
