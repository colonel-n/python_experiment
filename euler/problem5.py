#coding: UTF-8
# 2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.
# では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.

# 最大公約数
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
# 最小公倍数  
def lcm(a, b):
    return a * b / gcd(a, b)
base = lcm(19, 20)
num = 1
while True:
	val = num * base
	all_ok = True
	for i in range(1,19):
		if val%i != 0: 
			all_ok = False
			break
	if all_ok:
		print val
		break 	
	num += 1