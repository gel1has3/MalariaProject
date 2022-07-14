# CreateQueryFasta

def CreateQueryFasta(file_name,IDs):
	
	import numpy as np
	from Bio import SeqIO
	from FindPeptide import *
	

	file_path = '../VectorProteins/'
	file = open(file_path+file_name+'.csv')
	peptide_codes = [line.strip() for line in file.readlines()]
	file.close()
	peptide_records = []
	k = 1
	for peptide_code in peptide_codes:
	    I,J = FindPeptide(peptide_code,IDs)
	    for l in np.arange(len(I)):
	        i = I[l]
	        j = J[l]
	        proteome = proteomes[j]
	        peptide = proteome[i]
	        print k,short_names[j],peptide.id,i,j
	        peptide_records.append(peptide)
	    k = k + 1
	SeqIO.write(peptide_records,file_path+file_name+'.fasta','fasta')

