# ReadAlignmentScores.py

def ReadAlignmentScores(file_name,N):
	
	import numpy as np

	seq_id = np.zeros(N)
	seq_sim = np.zeros(N)
	gaps = np.zeros(N)
	scr = np.zeros(N)
	file = open(file_name)
	k1 = 0
	k2 = 0
	k3 = 0
	k4 = 0
	for line in file.readlines():
		line = line.strip()
		if line.find('Identity') >= 0:
			i = line.find('(')
			j = line.find('%')
			seq_id[k1] = float(line[i+1:j])
			k1 = k1 + 1
		if line.find('Similarity') >= 0:
			i = line.find('(')
			j = line.find('%')
			seq_sim[k2] = float(line[i+1:j])
			k2 = k2 + 1
		if line.find('Gaps') >= 0:
			i = line.find('(')
			j = line.find('%')
			gaps[k3] = float(line[i+1:j])
			k3 = k3 + 1
		if line.find('Score') >= 0:
			i = line.find(':')
			scr[k4] = float(line[i+1:])
			k4 = k4 + 1
	file.close()

	return seq_id,seq_sim,gaps,scr
