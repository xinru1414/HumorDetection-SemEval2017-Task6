import os
import csv

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

root_path = '/Users/xinru/Developer/Thesis/SemEval2017/Humor/trial_dir/trial_data_result'



for filename in listdir_nohidden(root_path):
	fullpath = os.path.join(root_path, filename)
	if fullpath.endswith(".tsv"):
		outfile = fullpath.replace(".tsv", "") + '_PREDICT.tsv'
	#print(outfile)
	# read in file line by line
	with open(fullpath,'r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		sortedlist = sorted(tsvin, key=lambda row: row[2], reverse=False)
		with open(outfile, 'w') as o:
			#o.write('\n'.join(map(str,sortedlist)))
			for i in range(len(sortedlist)):
				o.write(sortedlist[i][0] + "\n")