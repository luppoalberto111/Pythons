#Implement Number to Pattern
#Input
index = 6215
k= 8
#Output : AGTC

def number_to_letter(index):
    if index == 0:
        letter = 'A'
    elif index == 1:
        letter = 'C'
    elif index == 2:
        letter = 'G'
    elif index == 3:
        letter = 'T'
    return letter

def number_to_pattern(index,k):
    if k == 1:
        return number_to_letter(index)

    prefix_index = index/4
    r = index%4
    prefix_pattern  = number_to_pattern( prefix_index, k - 1 )
    letter = number_to_letter(r)

    return prefix_pattern + letter
print number_to_pattern(index, k)