# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# April 2018
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program reads in all the tweets and outputs files accordingly with pre_processed tweet

# Language: Python 2.7
# Command line example:
#	python pre_tweet.py lm_train_dir/lm_train_data lm_train_dir/lm_train_data_pre 
# Output tweet example (each tweet is on its own line) for all pre_process settings
# (removing urls, removing tokens startting with @ and #, lowercasing and tokenization)
# 	730821754575167488	awkward sex request ?
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
# import 
import sys, os
import csv
import re
from string import punctuation

# read in all files from train_dir/train_data. Change the path to your own path
#root_path = 'train_dir/train_data'
root_path = sys.argv[1]
# outputs all tweets in a plain txt file
#outfile = 'plain.txt'
result_path = sys.argv[2]

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

for filename in listdir_nohidden(root_path):
	fullpath = os.path.join(root_path, filename)
	outfilefullpath = os.path.join(result_path, filename)
	outfile = outfilefullpath
	with open(fullpath,'r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		with open(outfile, 'w') as tsvout:
			writer = csv.writer(tsvout, delimiter='\t')
			for row in tsvin:
					# getting rid of urls in the tweet
					rt = re.sub(r'http\S+', '', str(row[1]), flags=re.MULTILINE)
					# getting rid of tokens started with @ (names)
					rt = re.sub(r'\s?@\w+\s?', ' ', rt, flags=re.MULTILINE)
					# getting rid of tokens started with # (hashtags)
					#rt = re.sub(r'\s?#\w+\s?', '', rt, flags=re.MULTILINE)
					# remove all punctuations
					#rt = ''.join(c for c in rt if c not in punctuation)
					# remove leading space
					rt = rt.lstrip()
					# remove trailing space
					rt = rt.rstrip()
					# lowercase
					rt = rt.lower()
					#rt = re.sub(r'#pointsme', '', rt)
					#tokenization
					rt = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", rt)
					rt = re.sub('(?<! )(?=[.,!?()])|(?<=[.,!?()])(?! )', r' ', rt)
					rt = re.sub(r'\"', '', rt, flags=re.MULTILINE)
					rt = re.sub(r'# ', '#', rt, flags=re.MULTILINE)
					writer.writerow([row[0], rt])
##### Program ends here #####
