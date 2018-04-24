# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Mar 2018
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program reads a text file (news), pre_process it and generates an output file for the same content
# Each sentence from the news is on a seperate line
# pre_process has two steps:
# 1) seperate punctuations
# 2) lower_case everything 
#
# Language: Python 3.5
# Command line example:
#	python3 pre_process.py INPUT_FILE OUTPUT_FILE
# example input:
#	i don’t get your point.
#	even in defeat, with the current commission remaining in office, its credibility may be fatally weakened for the last 11 months of its term in office.
# example output:
# 	i don’t get your point .
#	even in defeat , with the current commission remaining in office , its credibility may be fatally weakened for the last 11 months of its term in office .
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

import sys, os
import re
from string import punctuation

infile = sys.argv[1]
outfile = sys.argv[2]

def main():
	with open(infile, "r", encoding='UTF-8') as f:
		lines = f.readlines()
	with open(outfile, 'w') as o:
		for line in lines:
			# remove all punctuations
			#s = ''.join(c for c in line if c not in punctuation)
			# remove leading space
			s = line.lstrip()
			# remove trailing space
			s = s.rstrip()
			# tokenization
			s = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", line)
			s = re.sub('(?<! )(?=[.,!?()])|(?<=[.,!?()])(?! )', r' ', s)
			s = re.sub(r'\"', '', s, flags=re.MULTILINE)
			# lowercase
			o.write(s.lower()+'\n')
			#o.write(s+'\n')

if __name__ == '__main__':
    main()