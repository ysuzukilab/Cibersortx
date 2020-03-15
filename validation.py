#!/usr/bin/env python

import sys
import pandas as pd
from itertools import combinations

'''
Mix two cell types; combination of all cell types
python validation.py ../raw_data/MCA_liver_cell_expression_phenotype.tsv 
'''

def func(df,df_output,celltype1,celltype2):

	celltype1_list = []
	celltype2_list = []
	for c in df.columns:
		celltype = c.split('.')[0]
		if celltype == celltype1:
			celltype1_list.append(c)
		elif celltype == celltype2:
			celltype2_list.append(c)

	series_1 = df[celltype1_list].sum(axis=1)/len(celltype1_list)
	series_2 = df[celltype2_list].sum(axis=1)/len(celltype2_list)
	series = series_1 + series_2
	df_new = series.to_frame()

	l = sorted([celltype1,celltype2])	
	df_new.columns = ['_'.join(l)]

	return pd.concat([df_output,df_new],axis=1)


def main():

	df_input = pd.read_csv(sys.argv[1],index_col=0,sep='\t',low_memory=False)
	all_celltypes = []
	for c in df_input.columns:
		if '.' not in c:
			all_celltypes.append(c)
	comb = combinations(all_celltypes,2)
	df_output = pd.DataFrame(index=df_input.index.copy())
	for c in list(comb):
		df_output = func(df_input,df_output,c[0],c[1])

	s = 'validation.tsv'
	df_output.to_csv(s,sep='\t')


if __name__ == '__main__':
	main()

