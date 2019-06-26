# codon optimize for C. ljungdahlii
def codon_convert(input_sequence):
	assert type(input_sequence) == str, "Error, input must be a DNA sequence."
	import textwrap
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
