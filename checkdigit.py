#coding: UTF-8
import sys
import re

input_line = sys.stdin.readline().rstrip()
length = len(input_line)
if not length in {12,7,13,11}:
	print(u"チェックディジットの値ではない")
	exit()
	
arr = list(input_line[::-1])
even = 0
odd = 0
for i in range(length):
	if i%2 == 0:
 		even += int(arr[i])	
	else:
 		odd += int(arr[i])
result_arr = tuple(str(even * 3 + odd))
check_digit = str(10 - int(result_arr[len(result_arr) - 1])) 
print u'チェックディジット:' + check_digit
print input_line + check_digit

	