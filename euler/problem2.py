#coding: UTF-8
# フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 数列の項の値が400万以下の, 偶数値の項の総和を求めよ.
list = []
total = 0
value = 0
num = 0
while value <= 4000000:
	if value%2 == 0:
		total += value	
	if len(list) < 3:
		value = num
		list.append(value)
	else:
		value = list[num-2]+list[num-1]
		list.append(value)
	num += 1	
print total