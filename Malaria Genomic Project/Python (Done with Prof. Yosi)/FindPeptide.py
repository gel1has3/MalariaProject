# FindPeptide.py

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
