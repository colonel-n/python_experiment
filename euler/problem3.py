#coding: UTF-8
# 13195 の素因数は 5, 7, 13, 29 である.
# 600851475143 の素因数のうち最大のものを求めよ.
def prime_factorization(n):
  i = 2
  arr = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      arr.append(i)
    i += 1
  if n > 1:
    arr.append(n)
  return arr
print prime_factorization(600851475143)[-1]