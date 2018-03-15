i = 1
f= open('/Users/phudang/Desktop/rosalind_ini5-2.txt', 'r')

for line in f:
	if i % 2 ==0:
		print line
	i = i +1