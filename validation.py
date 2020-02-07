#!/usr/bin/env python

import sys
import pandas as pd

'''
Mix two cell types 
python validation.py ../raw_data/MCA_liver_cell_expression_phenotype.tsv Hepato B
'''

def main():
	df = pd.read_csv(sys.argv[1],header=None,index_col=0,sep='\t',low_memory=False)
	celltype1 = sys.argv[2]
	celltype2 = sys.argv[3]
	celltype1_list = []
	celltype2_list = []
	for c in df.columns:
		celltype = df.loc[df.index.isnull(),c].values[0]
		if celltype == celltype1:
			celltype1_list.append(c)
		elif celltype == celltype2:
			celltype2_list.append(c)
	#print(celltype1_list)
	#print(celltype2_list)
	s = 'validation_'+sys.argv[2]+'_'+sys.argv[3]+'.tsv'
	#s = sys.argv[1].split('.')[0]+'_'+sys.argv[2]+'_'+sys.argv[3]+'.tsv'
	df[celltype1_list+celltype2_list].to_csv(s,sep='\t',header=False)

if __name__ == '__main__':
	main()

