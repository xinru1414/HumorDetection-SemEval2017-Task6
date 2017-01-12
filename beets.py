import sys, os
import kenlm
import csv
import re

# do not read hidden files in the folder
def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

# the Language Model trained on the trainig data
LM = "/Users/xinru/Developer/Thesis/src/kenlm/build/text.arpa"
model = kenlm.Model(LM)

root_path = '/Users/xinru/Developer/Thesis/SemEval2017/Humor/trial_dir/trial_data'
result_path = '/Users/xinru/Developer/Thesis/SemEval2017/Humor/trial_dir/trial_data_result'

for filename in listdir_nohidden(root_path):
	fullpath = os.path.join(root_path, filename)
	if filename.endswith(".tsv"):
		filename = filename.replace(".tsv", "")
	outfilefullpath = os.path.join(result_path, filename)
	outfile = outfilefullpath + '.tsv'
	# read in file line by line
	with open(fullpath,'r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		with open(outfile, 'w') as tsvout:
			writer = csv.writer(tsvout, delimiter='\t')
			for row in tsvin:
				# raw tweet (without links)
				rt = re.sub(r'https?:\/\/.*', '', str(row[1]), flags=re.MULTILINE)
				# score based on the language model for each tweet
				writer.writerow([row[0], row[1], model.score(rt)])