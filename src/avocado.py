# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Jan 2017
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program reads in all the tweets in the training data which the task provides from train_dir/train_data and outputs a plain text file for later language model to use.
# You can find training data here: http://alt.qcri.org/semeval2017/task6/index.php?id=data-and-tools

# Language: Python 2.7
# Command line example:
#	python avocado.py lm_train_dir/lm_train_data plain.txt
# Output file: (each tweet is on its own line)
# 	Rollin' Atkinson #420Celebs @midnight
#	@midnight Jon Bong Jovi #420celebs
#	@midnight Nug Benson #420Celebs
#	Gwen Spliffani #420Celebs @midnight

##### Program starts here #####
# import 
import sys, os
import csv
import re

# read in all files from train_dir/train_data. Change the path to your own path
#root_path = 'train_dir/train_data'
root_path = sys.argv[1]
# outputs all tweets in a plain txt file
#outfile = 'plain.txt'
outfile = sys.argv[2]


with open(outfile, 'w') as o:
	for filename in os.listdir(root_path):
		fullpath = os.path.join(root_path, filename)
		with open(fullpath,'r') as tsvin:
			# read in file as csv
			tsvin = csv.reader(tsvin, delimiter='\t')
			for row in tsvin:
				# getting rid of urls in the tweet
				row = re.sub(r'https?:\/\/.*', '', str(row[1]), flags=re.MULTILINE)
				#row = row.lower()
				o.write(row + '\n')
##### Program ends here #####
