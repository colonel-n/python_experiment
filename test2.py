tag_a,tag_b = raw_input().rstrip().split()
s = raw_input().rstrip()
while len(s) > 0:
	s_index = s.find(tag_a)
	if s_index < 0:
		break
	s = s[(s_index + len(tag_a)):]
	e_index = s.find(tag_b)
	if e_index < 0:
		break
	tmp = s[:e_index]
	print tmp if len(tmp) > 0 else '<blank>'
	s = s[(e_index + len(tag_b)):]