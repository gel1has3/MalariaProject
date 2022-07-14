# MalariaProject
This project was developed in partnership with Prof. Yosi Shibbru (Rose-Hulman Institute of Technology, USA).

The result of this project was presented on ISCB Africa ASCBCB Conference on Bioinformatics, March 9-11, 2015, Daressalaam, Tanzania and BLACK IN AI WORKSHOP co-located with NIPS 2018 at the Palais des Congrès de Montréal (Montreal Convention Centre) in Montréal CANADA on December 7th. 2018.

About Malaria

Only 60 of the 450 known species of Anopheles mosquito transmit malaria. The genetic diversity of these 60 mosquitoes with respect to the other 390 non- transmitters suggests that the capacity to transmit malaria was acquired independently for each species through a process of convergent evolution. Despite a complex process of species, co-evolution of Plasmodium parasites and corresponding Anopheles mosquitoes, some interactions are believed to be conserved across all parasite-mosquito combinations that support malaria transmission.


Recently, Biology and Medicine are rapidly becoming data intensive. A recent comparison of genomics with social data, online videos and other data intensive discipline suggests that genomics alone will equal or surpass other fields in data generation and analysis within the next decade.
New Volume New Complex New Challenge and Opportunities such as  Possibility for rational vaccine design strategies

In this project, 

1. We collected 94 genes. Sreenivasamurthy et al. have compiled a list of 94 genes distilled from 55 publications. Each gene has been experimentally verified to affect Anopheles gambiae-Plasmodium interactions at various stages of Plasmodium’s lifecyle in Anopheles gambiae, as measured by number of surviving oocysts, rate of ookinetes melanization and number of sporozoites.

2. Classify 16 Anopheles species each of which has been classified as either a major or a minor/non-vector for malaria.
3. Then, for each of 119 Anopheles gambiae mosquito proteins known to affect malaria transmission, we selected a corresponding ortholog (if any existed) in each of the remaining 18 Anopheles mosquito species
4.  As a measure of the relevance of each protein residue to malaria transmission, we computed an alignment column conservation index between -1 and 1.  -1 indicates that he protein residue is exclusively conserved in minor/non-transmitters and 1 indicates that it is exclusively conserved in major transmitters.
5.  For each residue, we also computed a log-odds ratio. Large positive log-odds ratios indicate a high probability the residue is from a major transmitter and large negative values indicate a high probability the residue is from a minor/non-transmitter of malaria. 
6. Because the number of attributes (number of residues) is much larger than the number of records (number of mosquitoes) a dimensionality- reduction methods must be used.
7. We applied principle component analysis to each of the 119 multiple sequence alignments to cluster alignment columns into 19 principle component vectors. Then, we applied principle component analysis to each of the 119 multiple sequence alignments to cluster alignment columns into 19 principle component vectors. Each principle component vector represents a cluster of multiple sequence alignment columns. Each vector is weighted by its PVE (proportion of variance). PVE is a measure of the signal strength of the principle component. A PVE equal to 0 indicates there is little to no variation between mosquito species within the corresponding alignment column principle component cluster where as a 1 indicates most of the variation in the alignment between mosquito species is concentrated in the corresponding principle component alignment column cluster.
8. Next, We use two measures of the relevance of each principle component to malaria transmission: The cosine of the angle (abbreviated dcos for direction cosine) between the principle component vector and the ideal malaria vector is an indication of the specificity of the principle component to malaria transmission. The component of the projection of the principle component vector in the direction of the ideal malaria vector is equal to the product of PVE and dcos and is a measure of both signal strength and malaria specificity.  
9. Finally, to assess statistical significance, we applied a permutation test to each measure. 
10. In the end,  using the constructed dataset we employed decision tree (ML). SMOTE is employed to handle the dataset imbalance.

 


