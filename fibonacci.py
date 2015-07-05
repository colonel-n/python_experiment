#coding: UTF-8

list = []
for i in range(10):
	list.append(i) if len(list) < 3 else list.append(list[i-2]+list[i-1])		
print list