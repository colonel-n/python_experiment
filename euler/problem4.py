#coding: UTF-8
# 左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
# では, 3桁の数の積で表される回文数の最大値を求めよ.
def digit_multiplication_check(target):
	list = range(100,1000)
	list.reverse()
	for i in list:
		for j in list:
			result = i * j
			if result == target:
				return True
			elif result < target:
				break
	return False		

max_num = 999 * 999
minimun_num = 100 * 100
val = max_num
target = 0 
while val >= minimun_num:
	tmp = str(val)
	length = len(tmp)
	left_end = length/2
	if length%2 == 0:
		right_start = length/2
	else:
		right_start = length/2 + 1
	if tmp[0:left_end] == tmp[right_start:length][::-1]:
		
		if digit_multiplication_check(val):
			target = val
			break
	val -= 1
print target