# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
m,n,k = map(int,raw_input().rstrip().split())
candidates = {}
for i in range(k):
	vote = raw_input().rstrip()
	if candidates.has_key(vote):
		candidates[vote] += 1
	else:
		candidates[vote] = 1
	for key in candidates:
		if key == vote or candidates[key] <=0:
			continue
		candidates[key] -= 1
		candidates[vote] += 1
max = max(candidates[x] for x in candidates)
for key in sorted(candidates):
	if candidates[key] == max:
		print key
	
		