#Open Reading Frames
#DNA 5' ->3'
with open('input.txt') as f:
    t= "".join(line.strip() for line in f)  
#print t

#t = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

#Transcribing DNA into RNA(RNA1)
def transcription(t):
	rna = t.replace('T', 'U')
	return rna
#print transcription(t)

rna1 = transcription(t)

#Reserve Complement
def reverse_complement(t):
	d = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
	r =''
	for i in t:
		r+=d[i]
	return r[::-1]
#print reverse_complement(t)
rna2= reverse_complement(t)
rna2 = transcription(rna2)

#Translate an RNA String into an Amino Acid String
def create_codon_table():
	codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    		"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    		"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    		"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    		"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    		"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    		"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    		"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    		"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    		"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    		"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    		"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    		"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    		"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    		"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    		"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
	return codons

def translate(t):
	codons = create_codon_table()
	protein =''
	for i in xrange(0, len(t)-2,3):
		protein += codons[t[i:i+3]]
	return protein
#print translate(t)

#Open_reading_frames
s =[]
def open_reading_frames(t):
	for i in xrange(0,len(t)):
		index_1 = t.find('M',i)
		i +=index_1+1
		index_2 = t.find('STOP',index_1+1)
		
		if index_2>0 and index_1>0:
			s = t[index_1 : index_2 + 1]
		#print s
	return s
#print open_reading_frames(t)

translation_rna1 = translate(rna1)
translation_rna2 = translate(rna2)
translation_rna1_2= translate(rna1[1:len(rna1)])
translation_rna2_2 = translate(rna2[1:len(rna2)])
translation_rna1_3= translate(rna1[2:len(rna1)])
translation_rna2_3 = translate(rna2[2:len(rna2)])
#print translation_rna1
#print translation_rna2
#print translation_rna1_2
#print translation_rna2_2
#print translation_rna1_3
#print translation_rna2_3
list1 = open_reading_frames(translation_rna1)
list2 = open_reading_frames(translation_rna2)
list3 = open_reading_frames(translation_rna1_2)
list4 = open_reading_frames(translation_rna2_2)
list5 = open_reading_frames(translation_rna1_3)
list6 = open_reading_frames(translation_rna2_3)
print list1
print list2
print list3
print list5
print list4
print list6