# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Jan 2017
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program reads in the hashtag files, generates a score for each tweet and outputs a tsv file contianing the tweet_id, tweet and the score for each hashtag file.
# 

# Language: Python 2.7
# Command line example:
#	python beets.py
# Outputfile example: #BadInventions.tsv 
# Format: tweet_id		tweet        												language model score
#	651794322560581632	Battery Operated Wet Dream Goggles #BadInventions @midnight	-27.781261444091797
#	651783489646411776	#BadInventions @midnight cigarette scented air freshener	-27.478612899780273
#	651601127432192000	@midnight hashtag games #BadInventions jk but please use this on the show	-40.52326965332031
#	651772852333490176	Pumpkin Spice Viagra  #BadInventions @midnight	-15.142515182495117

##### Program starts here #####
import sys, os
# the kenlm languge model
import kenlm
import csv
import re

# do not read hidden files in the folder
def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

# load the Language Model trained on the trainig data. Change the path to your own path
LM = "/Users/xinru/Developer/Thesis/src/kenlm/build/text.arpa"
model = kenlm.Model(LM)

# input file path. Change the path to your own path
root_path = '/Users/xinru/Developer/Thesis/SemEval2017/Humor/trial_dir/trial_data'
# output file path. Change the path to your own path
result_path = '/Users/xinru/Developer/Thesis/SemEval2017/Humor/trial_dir/trial_data_result'

# read in the file
for filename in listdir_nohidden(root_path):
	fullpath = os.path.join(root_path, filename)
	if filename.endswith(".tsv"):
		filename = filename.replace(".tsv", "")
	outfilefullpath = os.path.join(result_path, filename)
	# name the output file as the same as input file
	outfile = outfilefullpath + '.tsv'
	with open(fullpath,'r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		with open(outfile, 'w') as tsvout:
			writer = csv.writer(tsvout, delimiter='\t')
			for row in tsvin:
				# raw tweet (without urls)
				rt = re.sub(r'https?:\/\/.*', '', str(row[1]), flags=re.MULTILINE)
				#count = len(re.findall(r'\w+', rt))
				# score based on the language model for each tweet
				writer.writerow([row[0], row[1], model.score(rt)])
##### Program ends here #####