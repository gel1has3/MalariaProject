# AlignPeptides.py

def AlignPeptides(query_file,proteome_file,output_file):
	
	from Bio import SeqIO
	from Bio.Emboss.Applications import NeedleCommandline
	
	
	file_name = 'OocystAgonist'
	
	query_path    = '../VectorProteins/'
	proteome_path = '../Peptide_Dataset/'
	
	file = open(proteome_path+'file_list.txt')
	proteome_files = [line.strip() for line in file.readlines()]
	file.close()
	
	# create temporary query fasta file
	file = open(query_path+file_name+'.fasta')
	query_peptides = list(SeqIO.parse(file,'fasta'))
	file.close()
	
	file = open(proteome_path+proteome_files[0])
	proteome_peptides = list(SeqIO.parse(file,'fasta'))
	
	query = query_peptides[0]
	SeqIO.write(query,'query.fasta','fasta')
	
	cline = NeedleCommandline()
	cline.asequence = 'query.fasta'
	cline.bsequence = proteome_path+proteome_files[0] 
	cline.gapopen = 10
	cline.gapextend = 0.5
	cline.outfile = 'needle.txt'
	stdout,stderr = cline()
	print stdout + stderr
