N,A,B = list(map(int,input().split()))
S = input()
kokunai = 0
kaigai = 0
cnt = 0
for s in S:
    if s == "a":
        if cnt < A + B:
           print("Yes")
           cnt += 1
        else:
            print("No")
    
    elif s == "b":
        kaigai += 1
        if cnt < A + B and kaigai <= B:
            print("Yes")
            cnt += 1
        else:
            print("No")
    else:
        print("No")
   