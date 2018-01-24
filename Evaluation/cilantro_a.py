# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Jan 2017
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program is for Task_A. It predicts which tweet is funnier for every possible combination of tweet pairs from a given hashtag file. To be more specific, it takes in the results for each hashtag file from beets.py and for each hashtag file it outputs a file that contain prediction for each possible pair of tweets. The output file format meets the Evaluation criteria, showed as follows:
#	<tweet1_id>\t<tweet2_id>\t<prediction>\n
#	where <prediction> is 1 if the first tweets is funnier and 0 otherwise.
	
# Language: Python 2.7
# Command line example:
#	python src/cilantro_a.py mydata/lm_train_result/lm_score/ news
# Output file example: #BadInventions.tsv 
#	651782900413792257	651787332107022336	1
#	651782900413792257	651777234198495232	1
#	651782900413792257	651602018176364544	0
#	651782900413792257	651772852333490176	1
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
import os
import csv
import itertools,sys
import random

# do not read hidden files in the folder
def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

root_path = sys.argv[1]
# set up news data or tweets data
data = sys.argv[2]

for filename in listdir_nohidden(root_path):
	fullpath = os.path.join(root_path, filename)
	if fullpath.endswith(".tsv"):
		outfile = fullpath.replace(".tsv", "") + '_PREDICT.tsv'
		outfile = outfile.replace("lm_score", "A_lm")
	with open(fullpath,'r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		# sort the tweet based on the LM score they get
		# reverse = True for funny tweets 
		# reverse = False for news data
		sortedlist = sorted(tsvin, key=lambda row: float(row[2]), reverse=True)
		with open(outfile, 'w') as o:
			for a, b in itertools.combinations(range(len(sortedlist)), 2):
				# > for funny tweets
				# < for news data
				if data == 'tweets':
					if float(sortedlist[a][2]) > float(sortedlist[b][2]):
						o.write(sortedlist[a][0] + '\t' + sortedlist[b][0] + '\t' + '1' + '\n')
					else:
						o.write(sortedlist[a][0] + '\t' + sortedlist[b][0] + '\t' + '0' + '\n')
				else:
					if float(sortedlist[a][2]) < float(sortedlist[b][2]):
						o.write(sortedlist[a][0] + '\t' + sortedlist[b][0] + '\t' + '1' + '\n')
					else:
						o.write(sortedlist[a][0] + '\t' + sortedlist[b][0] + '\t' + '0' + '\n')

##### Program ends here #####


