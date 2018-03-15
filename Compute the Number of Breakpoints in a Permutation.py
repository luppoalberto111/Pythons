#Number of Breakpoints Problem
f = open('input.txt','r')
#input6: (-3 +4 +1 +5 -2)
new_line= f.readline().rstrip('\n')
strip_right= new_line.rstrip(')')
strip_left = strip_right.lstrip('(')
permutation = strip_left.split(' ')

per =[]
for i in permutation:
	per.append(int(i))
# print per
per = [0] + per+ [len(per)+1]
	
count =0
for i in xrange(0, len(per)-1):
	if per[i] + 1 != per[i+1]:
		count +=1
print count