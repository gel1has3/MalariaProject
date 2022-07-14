# ProteomeHeatmaps.py

import numpy as np
from Bio import SeqIO
import malaria

file = open('../Peptide_Dataset/file_list.txt')
proteome_files = [line.strip() for line in file.readlines()]

file = open('../VectorProteins/OocystAgonist.fasta')
query_peptides = list(SeqIO.parse(file,'fasta'))

query = query_peptides[0]
SeqIO.write(query,'query.fasta','fasta')

malaria.AlignPeptides('query.fasta','../Peptide_Dataset/'+proteome_files[0],'needle.txt')

file = open('../Peptide_Dataset/'+proteome_files[0])
proteome = list(SeqIO.parse(file,'fasta'))
N = len(proteome)

seq_id,seq_sim,gaps,scr = ReadAlignmentScores('needle.txt',N)
