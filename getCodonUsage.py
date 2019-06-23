def getCodonUsage(DNAsequence):
  assert type(self.sequence) == str, 'Input must be DNA sequence(s)' 
  assert len(self.sequence)%3 == 0, 'Input sequence must encode a gene/ divisible by 3'
  # Note that this is the standard codon table but some organisms may have different codon usage such as TAG codes for selenocysteine instead of a stop codon.
	CodonTable = {'TTT':'Phe','TTC':'Phe','TTA':'Lue','TTG':'Lue','CTT':'Lue','CTC':'Lue','CTA':'Lue','CTG':'Lue',
					'ATT':'Ile','ATC':'Ile','ATA':'Ile','ATG':'Met','GTT':'Val','GTC':'Val','GTA':'Val','GTG':'Val','TCT':'Ser','TCC':'Ser',
					'TCA':'Ser','TCG':'Ser','CCT':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro','ACT':'Thr','ACC':'Thr','ACA':'Thr',
					'ACG':'Thr','GCT':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala','TAT':'Tyr','TAC':'Tyr','TAA':'Terminator','TAG':'Terminator',
					'CAT':'His','CAC':'His','CAA':'Gln','CAG':'Gln','AAT':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys','GAT':'Asp','GAC':'Asp',
					'GAA':'Glu','GAG':'Glu','TGT':'Cys','TGC':'Cys','TGA':'Terminator','TGG':'Trp','CGT':'Arg','CGC':'Arg','CGA':'Arg',
					'CGG':'Arg','AGT':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg','GGT':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}
	import textwrap
	chuncks_of_three = textwrap.wrap(DNAsequence, 3)
	collection = {}
	for bases in chuncks_of_three:
		if bases not in collection:
			collection[bases] = 0
		collection[bases] += 1
	CodonAndNumber = {}
	for key in CodonTable:
		if key in collection:
			CodonAndNumber [key] = (CodonTable[key], collection[key])
		else:
			CodonAndNumber[key] = (CodonTable[key], 0)
	import pandas
	CodonAndNumber_df = pandas.DataFrame(CodonAndNumber)
	CodonAndNumber_df = CodonAndNumber_df.transpose()
	new_collection = {}
	for codon in CodonAndNumber_df[0]:
		new_collection[codon] = CodonAndNumber_df[1][CodonAndNumber_df[0] == codon].sum()
	codon_list = list(CodonAndNumber_df[0])
	frequency = []
	for i in range(len(CodonAndNumber_df)):
		frequency.append(new_collection[codon_list[i]])
	CodonAndNumber_df[2] = frequency
  # assign 0 to column 3 as the placeholder
	CodonAndNumber_df[3] = 0
	for i in range(len(CodonAndNumber_df)):
		if CodonAndNumber_df[2][i] != 0:
			CodonAndNumber_df[3][i] = 100*CodonAndNumber_df[1][i]/CodonAndNumber_df[2][i]
		    
	CodonAndNumber_df.columns = ['amino_acids', 'numbers_in_the_gene', 'total_of_the_aa', 'percentage_used']
    
	print(CodonAndNumber_df)
