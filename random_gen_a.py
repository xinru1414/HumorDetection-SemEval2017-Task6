# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Jan 2017
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program serves as baseline for Task A. It is similar to cilantro_a.py except for it predicts which tweet is funnier in a tweet pair randomly.

# Language: Python 2.7
# Command line example:
#	python random_gen_a.py
# Output file example: #BadInventions.tsv 
#	651782900413792257	651787332107022336	1
#	651782900413792257	651777234198495232	1
#	651782900413792257	651602018176364544	0
#	651782900413792257	651772852333490176	1

##### Program starts here #####
import os
import csv
import itertools
import random

# do not read hidden files in the folder
def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

# input file folder. Change the path to your own path
root_path = '/Users/xinru/Developer/Thesis/SemEval2017/Humor/trial_dir/trial_data_result'

for filename in listdir_nohidden(root_path):
	fullpath = os.path.join(root_path, filename)
	if fullpath.endswith(".tsv"):
		outfile = fullpath.replace(".tsv", "") + '_PREDICT.tsv'
	with open(fullpath,'r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		sortedlist = sorted(tsvin, key=lambda row: float(row[2]), reverse=True)
		with open(outfile, 'w') as o:
			for a, b in itertools.combinations(range(len(sortedlist)), 2):
				# random generates 0s and 1s
				if sortedlist[a][2] > sortedlist[b][2]:
					o.write(sortedlist[a][0] + '\t' + sortedlist[b][0] + '\t' + str(random.randint(0,1)) + '\n')
				# randomly generates 0s and 1s
				else:
					o.write(sortedlist[a][0] + '\t' + sortedlist[b][0] + '\t' + str(random.randint(0,1)) + '\n')
##### Program ends here #####