N,K = map(int,input().split())
p = list(map(int,input().split()))

#累積和を使う
e_s = [0] * (N+1)
for i in range(N):
    # 期待値の計算
    e = (p[i]+1)/2
    e_s[i+1] = e_s[i] + e

ans = 0
for j in range(N-K+1):
    ans = max(ans,e_s[j+K]-e_s[j])
print(ans)


    