### Cibersortx pipeline

#### input files   
single cell reference matrix  
class matrix  
  
-> convert_reference_file.py  
	convert header of reference file; replace sample name with cell phenotype  

#### Cibersortx  
construct signature matrix  

Mixture matrix  
  
-> filter_by_signature_genes.py  
	filter out samples with no expression for all the signature genes


