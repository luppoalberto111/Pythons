#Implement GreedySorting
f = open('input.txt','r')
#input6: (-3 +4 +1 +5 -2)
new_line= f.readline().rstrip('\n')
strip_right= new_line.rstrip(')')
strip_left = strip_right.lstrip('(')
permutation = strip_left.split(' ')

per =[]
for i in permutation:
	per.append(int(i))

# 1.function in_correct_position
def in_correct_position(index, value):
	if(abs(value) == index + 1):
		return True
	else:
		return False
		 	
# print in_correct_position(0,-3)
# print in_correct_position(0, 1)
# print in_correct_position(0,-1)

# 2.function find_index_of_correct_element
def find_index_of_correct_element(index,per_list):
	for i in xrange(len(per_list)):
		if index + 1  == abs(per_list[i]):
			return i
 	 
# print find_index_of_correct_element(0, [3,-1,4,-2,5])
# print find_index_of_correct_element(3, [1,2,3,-5,4])

# 3.function reverse_elements
def reverse_elements(s_index, e_index, per_list):
	out = per_list[:]
	for i in xrange(s_index,e_index + 1):
		out[i]= - per_list[e_index - (i - s_index)]
	return out
	
# a = [3,-1,4,2,5]
# print reverse_elements(0,1, a)
# print a
# print reverse_elements(2,4,[1,2,-4,-5,3])

# .4 function print_permutation
def print_permutation(per_list):
	out = ""
	for i in per_list:
		if i > 0:
			out += "+"
		out += str(i) + " "
	print "(" + out[:-1] + ")"
# print_permutation([1, 2, -4, -5, 3])
 
for i in xrange(len(per)):
	# print "======== Iteration " + str(i) + " value " + str(per[i])
	
	if not in_correct_position(i, per[i]):
		# print (in_correct_position(i, per[i]))
		ind = find_index_of_correct_element(i, per)
		# print "correct index: "  +  str(ind)
		per = reverse_elements(i, ind , per)
		print_permutation(per)
		
	if per[i] < 0:
		# print "flip sign"
 		per[i] =  - per[i]
 		print_permutation(per)