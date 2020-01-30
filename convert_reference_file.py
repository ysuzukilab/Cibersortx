#!/usr/bin/env python

import pandas as pd
import sys
import subprocess

'''
20200128
python convert_reference_file.py MCA_liver_cell_expression.tsv MCA_liver_cell_class.tsv
input file 1: expression
input file 2: classes
'''
def main():
	s1 = 'cat '+ str(sys.argv[1])+ ' | sed -n 1p > classes_matrix.tsv' 
	subprocess.call(s1,shell=True)
	s2 = 'cat ' + str(sys.argv[2]) + ' >> classes_matrix.tsv'
	subprocess.call(s2,shell=True)
	df = pd.read_csv('classes_matrix.tsv',delimiter = '\t',index_col=0)	
	dct = {}
	for index in df.index:
		for column in df.columns:
			if df.loc[index,column] == 1:
				dct[column]=index
	df_exp = pd.read_csv(sys.argv[1],delimiter='\t',index_col=0)
	df_exp = df_exp.rename(columns=dct)
	df_exp.to_csv(sys.argv[1].split('.')[0]+'_phenotype.tsv',sep='\t')

	dct_count = {}
	for key in dct.keys():#key:tag, value:phenotype
		if dct[key] not in dct_count.keys():
			dct_count[dct[key]] = 1
		else:
			dct_count[dct[key]] +=1
	for key in dct_count.keys():
		print(key + '\t' + str(dct_count[key]))


if __name__ == '__main__':
	main()
