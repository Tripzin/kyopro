# B

A, B, M = map(int, input().split())
ref_p = list(map(int, input().split()))
mic_p = list(map(int, input().split()))

# X_i番目の冷蔵庫とY_i番目の電子レンジを同時に買うと支払い増額がC_i安くなる
X_Y_C = [list(map(int, input().split())) for _ in range(M)]

# 割引を使わない場合の最小値
ans = min(ref_p) + min(mic_p)
for x, y, c in X_Y_C:
    temp = ref_p[x-1] + mic_p[y-1] - c

    ans = min(temp, ans)
print(ans)
