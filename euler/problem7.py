#coding: UTF-8
# 素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.
# 10001番目の素数を求めよ.
def is_prime(n): 
  i = 2
  while i * i <=n:
    if n % i == 0:
      return False
    i += 1
  return True
arr = []
cnt = 2
while len(arr) < 10001:
	if is_prime(cnt):
		arr.append(cnt)
	cnt += 1
print arr[-1]