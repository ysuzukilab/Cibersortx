#!usr/bin/env python

import sys
import pandas as pd

'''
could've used shell script
python filter_by_sig_genes.py ../output/signature_matrix/CIBERSORTx_Job15_MCA_liver_cell_expression_phenotype_inferred_refsample.txt ../input/MCA_liver_cell_expression_phenotype.tsv
python filter_by_sig_genes.py ../output/signature_matrix/CIBERSORTx_Job15_MCA_liver_cell_expression_phenotype_inferred_phenoclasses.CIBERSORTx_Job15_MCA_liver_cell_expression_phenotype_inferred_refsample.bm.K999.txt ../input/180627_liver_all_counts.tsv
'''


def main():
	df_sig = pd.read_csv(sys.argv[1],index_col=0,sep='\t')
	df_mix = pd.read_csv(sys.argv[2],index_col=0,sep='\t')
	df_mix_filtered = df_mix.filter(items=df_sig.index.values,axis=0)
	df_mix_filtered = df_mix_filtered.loc[:, (df_mix_filtered != 0).any(axis=0)]
	s = sys.argv[2].split('/')[-1].split('.')[0]+'_filtered.tsv'
	df_mix_filtered.to_csv(s,sep='\t')
if __name__ == '__main__':
	main()
