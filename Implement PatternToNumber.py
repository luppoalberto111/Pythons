#Implement Pattern to Number
pattern ='ACCATTTATCCTCGATCAAGCGGA'
    
def pattern_to_number(pattern):
	if pattern == "":
		return 0
		
	letter = pattern[len(pattern)-1]
	prefix = pattern[0:len(pattern)-1]
	
	if letter == "A":
		value_letter =0
	elif letter == "C":
		value_letter =1
	elif letter == "G":
		value_letter =2
	elif letter == "T":
		value_letter =3   
	
	return 4 * pattern_to_number(prefix) + value_letter
    
print pattern_to_number(pattern)