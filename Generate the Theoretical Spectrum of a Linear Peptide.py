#Generate the Theoretical Spectrum of a Linear Peptide
f = open('input.txt','r')
peptide = f.readline().rstrip()
pep_list = []
my_list = [0]

def linear_spectrum(peptide):
    s = ''
    table = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99,
             'T':101, 'C':103, 'I':113, 'L':113, 'N':114,
             'D':115, 'K':128, 'Q':128, 'E':129, 'M':131,
             'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
             
    s = table[peptide]
    return s
    
for i in xrange(len(peptide)):
    for j in xrange(len(peptide)):
        my_list1 = peptide[i:len(peptide)-j]
        if not my_list1 == '':
            pep_list.append(my_list1)
#print pep_list

for i in xrange(len(pep_list)):
    if len(pep_list[i]) == 1:
        my_list2 = 0
        for j in xrange(len(pep_list[i])):
            my_list2 += linear_spectrum(pep_list[i][j])
    elif len(pep_list[i]) > 1:
        my_list2 = 0
        for j in xrange(len(pep_list[i])):
            my_list2 += linear_spectrum(pep_list[i][j])
    my_list.append(my_list2)
#print my_list

linear_peptide = sorted(my_list)

for i in linear_peptide:
    print i,