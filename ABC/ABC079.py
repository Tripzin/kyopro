nums = list(map(int,list(input())))
for i in (-1,1):
  for j in (-1,1):
    for k in (-1,1):
      if nums[0]+nums[1]*i+nums[2]*j+nums[3]*k == 7:
        ans = str(nums.pop(0))
        for flag in (i,j,k):
          if flag == 1:
            ans += '+'
          else:
            ans += '-'
          ans += str(nums.pop(0))
        ans += '=7'
        print(ans)
        exit()
