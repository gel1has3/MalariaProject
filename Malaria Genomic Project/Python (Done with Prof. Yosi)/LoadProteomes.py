# LoadProteomes.py
 
import numpy as np

# read file names
from os import listdir
proteome_files = np.array(listdir('../Peptide_Dataset/'))

# sort file names by pylogeny 
proteome_files.sort()
index = np.array([9,3,11,19,18,5,7,13,17,15,8,10,6,16,12,4,2,1,14]) - 1
proteome_files = proteome_files[index]
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

# load proteomes
from Bio import SeqIO
IDs = []
proteomes = []
for file_name in proteome_files:
    file = open('../Peptide_Dataset'+'/'+file_name)
    proteome = list(SeqIO.parse(file,'fasta'))
    ID = [peptide.id for peptide in proteome]
    IDs.append(ID)
    proteomes.append(proteome)
    file.close()
