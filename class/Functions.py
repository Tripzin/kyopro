# ---------文字列を文字ごとカウントする-------- #
import string
from collections import Counter
s = 'HOGEHOGE'
c = Counter(s)
#  Counter({'H': 2, 'G': 2, 'O': 2, 'E': 2})
# ------------------------------------------ #


# -------------10**9+7で割った余りを返す-------#
def mod10_9_7(num):
    return num % (10**9+7)
# -------------------------------------------#


# ------------------------------------------#
# import string
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ------------------------------------------#

# ------------------整数か整数でないか---------#


def is_integer(num):
    for k in range(1, num+1):
        if k*k == num:
            return True
    else:
        return False
# ------------------------------------------#


# ---------------商と余りを同時に取得-----------#
q, mod = divmod(10, 3)
print(q, mod)
# 3 1
# ------------------------------------------#


# ---------素数判定---------------#
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#-------------------------------#


#-------------------------------#
from decimal import Decimal
# ２進数による丸め誤差を排除する
#-------------------------------#



#-------------重複----------------#
for i in range(2,N+1):
  X = (X**2) % M
  if p[X] != 0:
    repeat_start = p[X]
    repeat_end = i
    break
  else:
    sum[i] = sum[i-1] + X
    p[X] += i
#-------------------------------#