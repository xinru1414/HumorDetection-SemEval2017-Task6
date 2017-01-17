# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Jan 2017
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program serves as baseline for Task B. It is similar to cilantro_b.py except for it randomly produces a tweet_id list.

# Language: Python 2.7
# Command line example:
#	python random_gen_b.py
# Output file example: #BadInventions.tsv 
#	651782900413792257
#	651787332107022336
#	651777234198495232
#	651602018176364544

##### Program starts here #####
import os
import csv
import random

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

root_path = '/Users/xinru/Developer/Thesis/SemEval2017/Humor/trial_dir/trial_data'

for filename in listdir_nohidden(root_path):
	fullpath = os.path.join(root_path, filename)
	if fullpath.endswith(".tsv"):
		outfile = fullpath.replace(".tsv", "") + '_PREDICT.tsv'
	with open(fullpath,'r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		t_id = [row[0] for row in tsvin]
		# shuffle the tweet_id
		random.shuffle(t_id)
		#print(random.shuffle(t_id))
		with open(outfile, 'w') as o:
			for i in range(len(t_id)):
				o.write(t_id[i] + "\n")
##### Program ends here #####