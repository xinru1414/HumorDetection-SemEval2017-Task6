# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Jan 2017, updated on April 2018
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program reads in all the tweets in the pre processed training data and outputs a plain text file for later language model to use.
# You can find training data here: http://alt.qcri.org/semeval2017/task6/index.php?id=data-and-tools

# Language: Python 2.7
# Command line example:
#	python avocado.py lm_train_dir/lm_train_data_pre plain.txt
# Output file: (each tweet is on its own line)
# 	Rollin' Atkinson #420Celebs @midnight
#	@midnight Jon Bong Jovi #420celebs
#	@midnight Nug Benson #420Celebs
#	Gwen Spliffani #420Celebs @midnight
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
				o.write(row[1] + '\n')
##### Program ends here #####