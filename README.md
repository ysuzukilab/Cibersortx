### Cibersortx pipeline

#### input files   
single cell reference matrix  
class matrix  
  
-> convert_reference_file.py  
	convert header of reference file; replace sample name with cell phenotype  
```python
python convert_reference_file.py MCA_liver_cell_expression.tsv MCA_liver_cell_class.tsv
```
#### Cibersortx  
construct signature matrix  

Mixture matrix  
  
-> filter_by_signature_genes.py  
	filter out samples with no expression for all the signature genes

```python
python filter_by_signature_genes.py signature_gene_file.txt mixture_file.tsv
```
