#coding: UTF-8

def hanoi(num):
	if num == 1:
		return 1
	else:
		s = 2
		for i in range(0,num-1):
			s *= 2
		return s - 1		
num = int(input('数字を入力してください: '))
print hanoi(num)