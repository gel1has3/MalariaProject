# malaria.py 

import numpy as np
from Bio import SeqIO

# short mosquito names
short_names=[
'gambiae',
'arabiensis',
'quadriannulatus',
'merus',
'melas',
'christyi',
'epiroticus',
'stephensi',
'maculatus',
'culicifacies',
'funestus',
'minimus',
'dirus',
'farauti',
'sinensis',
'atroparvus',
'albimanus',
'Aedes',
'Culex'
]

def LoadProteomes():

	from os import listdir
	
	# create proteome file list
	dataset_path = '../ProteomeDataset/'
	proteome_files = np.array(listdir(dataset_path))
	
	# sort files by phylogeny 
	proteome_files.sort()
	index = np.array([9,3,11,19,18,5,7,13,17,15,8,10,6,16,12,4,2,1,14]) - 1
	proteome_files = proteome_files[index]
	file = open(dataset_path+'file_list.txt','w')
	for file_name in proteome_files:
		file.write(file_name+'\n')
	file.close()
	
	# load proteomes
	IDs = []
	proteomes = []
	for file_name in proteome_files:
	    file = open(dataset_path+file_name)
	    proteome = list(SeqIO.parse(file,'fasta'))
	    ID = [peptide.id for peptide in proteome]
	    IDs.append(ID)
	    proteomes.append(proteome)
	    file.close()

	return IDs, proteomes

def FindPeptide(peptide_code,IDs):
	I = []
	J = [] 
	j = 0
	for ID in IDs:
		i = 0
		for id in ID:
			if id.find(peptide_code)>=0:
				I.append(i)
				J.append(j)
			i = i + 1
		j = j + 1
	return I,J 

def CreateQueryFasta(file_name,IDs,proteomes,short_names):
	
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

def AlignPeptides(query_file,proteome_file,output_file):
	
	from Bio.Emboss.Applications import NeedleCommandline

	cline = NeedleCommandline()
	cline.asequence = query_file 
	cline.bsequence = proteome_file 
	cline.gapopen = 10
	cline.gapextend = 0.5
	cline.outfile = output_file 
	stdout,stderr = cline()
	#print stdout + stderr

def ReadAlignmentScores(file_name):
	
	seq_id = [] 
	seq_sim = []
	gaps = [] 
	scr = [] 
	file = open(file_name)
	for line in file.readlines():
		line = line.strip()
		if line.find('Identity') >= 0:
			i = line.find('(')
			j = line.find('%')
			seq_id.append(float(line[i+1:j]))
		if line.find('Similarity') >= 0:
			i = line.find('(')
			j = line.find('%')
			seq_sim.append(float(line[i+1:j]))
		if line.find('Gaps') >= 0:
			i = line.find('(')
			j = line.find('%')
			gaps.append(float(line[i+1:j]))
		if line.find('Score') >= 0:
			i = line.find(':')
			scr.append(float(line[i+1:]))
	file.close()

	return seq_id,seq_sim,gaps,scr

# ProteomeHeatmaps.py

query_dataset = 'OocystAgonist'

file = open('../ProteomeDataset/file_list.txt')
proteome_files = [line.strip() for line in file.readlines()]
file.close()

file = open('../VectorProteins/'+query_dataset+'.fasta')
query_peptides = list(SeqIO.parse(file,'fasta'))
file.close()

N = len(query_peptides)
k = 1
for query in query_peptides:
	max_id = []
	SeqIO.write(query,'query.fasta','fasta')
	if k==1:
		c = 'w'
	else: 
		c = 'a'
	results_file = open('../Results/'+query_dataset+'.txt',c)
	i = 0
	for file_name in proteome_files[0:2]:
		AlignPeptides('query.fasta','../ProteomeDataset/'+file_name,'needle.txt')
		seq_id,seq_sim,gaps,scr = ReadAlignmentScores('needle.txt')
		mx = max(seq_id)
		max_id.append(mx)
		print query.id,short_names[i],mx
		i = i + 1
	for r in max_id:
		results_file.write(str(r)+ ' ')
	results_file.write('\n')
	results_file.close()
	print k,'/',N
	k = k + 1
