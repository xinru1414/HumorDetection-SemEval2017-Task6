# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Jan 2017, updated on April 2018
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program reads in the pre processed hashtag files, generates a score for each tweet and outputs a tsv file contianing the tweet_id, tweet and the score for each hashtag file.
# 

# Language: Python 2.7
# Command line example:
#	python src/beets.py data/evaluation_dir/evaluation_data_pre mydata/lm_train_result/lm_score/ text.arpa
# Outputfile example: #BadInventions.tsv 
# Format: tweet_id		tweet        												language model score
#	651794322560581632	Battery Operated Wet Dream Goggles #BadInventions @midnight	-27.781261444091797
#	651783489646411776	#BadInventions @midnight cigarette scented air freshener	-27.478612899780273
#	651601127432192000	@midnight hashtag games #BadInventions jk but please use this on the show	-40.52326965332031
#
# This file is part of the Duluth system.
#
# The Duluth system is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The Duluth system is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the Duluth system.  If not, see <http://www.gnu.org/licenses/>.

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


# input file path. Change the path to your own path
root_path = sys.argv[1]
# output file path. Change the path to your own path
result_path = sys.argv[2]
# set up language model (arpar file)
LM = sys.argv[3]

model = kenlm.Model(LM)


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
				# score based on the language model for each tweet with normalization
				#writer.writerow([row[0], row[1], model.score(row[1], bos = True, eos = True)/len(row[1].rstrip().split(" "))])
				# no normalizaiton
				writer.writerow([row[0], row[1], model.score(row[1], bos = True, eos = True)])
				#writer.writerow([row[0], row[1], model.perplexity(row[1])])
##### Program ends here #####