# A
N = input()
N_i = int(N)
N_s = list(N)


for i in range(0,17):
  if N_i < 10 ** i:
    break
flag = True
for j in range(1,i):
  if N_s[j] != "9":
    flag = False
    break

if flag == True:
  # 最上位を除いたすべての桁が9
   print(int(N_s[0])+9*(len(N_s)-1))
else:
   print(int(N_s[0])+9*(len(N_s)-1)-1)





