def mv_plus(point,mv,limit):
    tmp = point + mv
    if tmp > limit:
        tmp = tmp -limit
    if tmp == limit:
    	return 0
    else:
		return tmp
        
def mv_minus(point,mv,limit):
    tmp = point - mv
    if tmp < 0:
        tmp = limit + tmp
    if tmp == limit:
    	return 0
    else:
		return tmp
        
w,h,n = map(int,raw_input().rstrip().split())
x,y = map(int,raw_input().rstrip().split())
for num in range(n):
    dir,m = raw_input().rstrip().split()
    m = int(m)
    if dir == 'U':
    	y = mv_plus(y,m,h)
    elif dir == 'D':
    	y = mv_minus(y,m,h)
    elif dir == 'R':
    	x= mv_plus(x,m,w)
    elif dir == 'L':
        x= mv_minus(x,m,w)
print "%d %d" % (x,y)