#Generate the Theoretical Spectrum of a Cyclic Peptide
f = open('input.txt','r')
peptide = f.readline().rstrip()
f.close()

def cyclic_spectrum(peptide):
    length = len(peptide)
    pepCount = length * (length - 1) + 1
    result = [0]
    table = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99,
             'T':101, 'C':103, 'I':113, 'L':113, 'N':114,
             'D':115, 'K':128, 'Q':128, 'E':129, 'M':131,
             'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
    for i in xrange(pepCount):
        if i % length == 0:
            peptide += peptide
        result.append(0)
        for char in peptide[i:i + i / length + 1]:
            result[-1] += table[char]
    result.sort()
    return result

f = open('output.txt','w')
for vals in cyclic_spectrum(peptide):
   f.write(str(vals) + ' ')
f.close()