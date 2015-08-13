# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

def make_regexp_from_ipaddr(target):
	if re.match("^[0-9]+$" , target):
		return target
	elif target == "*":
		return "[0-9]{1,3}"
	else:
		arr = target[1:-1].split("-")
		return "(%s)" % "|".join(map(str,range(int(arr[0]), int(arr[1]) + 1)))

ip_addr = raw_input().rstrip().split('.')
ip_regexp = re.compile("(%s\.%s\.%s\.%s)" % (ip_addr[0],ip_addr[1],make_regexp_from_ipaddr(ip_addr[2]),make_regexp_from_ipaddr(ip_addr[3])))
time_regexp = re.compile("\[(.+)\\s.+\]")
file_name_regexp = re.compile("\".+\\s(.+)\\sHTTP\/.+\"")
num = int(raw_input().rstrip())
for i in range(num):
	line = raw_input().rstrip()
	arr = line.split()
	if ip_regexp.search(arr[0]):
		print "%s %s %s" % (arr[0],time_regexp.search(line).group(1),file_name_regexp.search(line).group(1))