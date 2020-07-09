# codon optimize for C. ljungdahlii
import textwrap
def codon_convert1(input_sequence):
	assert type(input_sequence) == str, "Error, input must be a DNA sequence."
	input_sequence = input_sequence.upper()
	chuncks_of_three = textwrap.wrap(input_sequence, 3)
	dict = {'TTC':'TTT', 'TTG':'TTA', 'CTC':'TTA', 'CTA':'TTA','CTG':'TTA','ATC':'ATA','GTC':'GTA',
			'TCC':'TCA','TCG':'TCA','CCC':'CCA','CCG':'CCA','ACC':'ACA','ACG':'ACA','GCC':'GCA','GCG':'GCA',
			'TAC':'TAT','GAC':'GAT','CGT':'AGA','CGC':'AGA','CGA':'AGA','CGG':'AGA','AGC':'AGT','GGC':'GGA','GGG':'GGA'}
	converted_DNA = []
	for nucleotide in chuncks_of_three:
		if nucleotide in dict:
			converted_DNA.append(dict[nucleotide])
		else: 
			converted_DNA.append(nucleotide)
	return "".join(converted_DNA)


# codon optimize for Human. This is an example to remove CpG from the sequence
def codon_convert2(input_sequence):
	assert type(input_sequence) == str, "Error, input must be a DNA sequence."
  	input_sequence = input_sequence.upper()
  	chuncks_of_three = textwrap.wrap(input_sequence, 3)
  	converted_DNA = []
  	dict1 = {'TCG':'TCA','CCG':'CCA','ACG':'ACT','GCG':'GCT','CGT':'AGG','CGC':'AGA','CGA':'AGA','CGG':'AGG',} # replacing all the codons that have CpGs
  	dict2 = {'TTC':'TTT','CTC':'CTG','ATC':'ATT','GTC':'GTG',
          	 'TCC':'TCT','CCC':'CCT','ACC':'ACA','GCC':'GCT','TAC':'TAT','CAC':'CAT',
          	 'AAC':'AAT','GAC':'GAT','TGC':'TGT','AGC':'AGT','GGC':'GGG'} # replacing codons wth C at the end
  	for i in range(len(chuncks_of_three)):
    		if i+1 == len(chuncks_of_three): # for the last codon
      			if chuncks_of_three[i] in dict1:
        			converted_DNA.append(dict1[chuncks_of_three[i]])
      			else:
        			converted_DNA.append(chuncks_of_three[i])
    		elif chuncks_of_three[i] in dict1:
      			converted_DNA.append(dict1[chuncks_of_three[i]]) 
    		else:
      			if chuncks_of_three[i].endswith('C') and chuncks_of_three[i+1].startswith('G'): # if the codon ends with C and the next codon starts with G, the codon needs to be replaced
        			converted_DNA.append(dict2[chuncks_of_three[i]])
      			else:
        			converted_DNA.append(chuncks_of_three[i])
	return ''.join(converted_DNA)
