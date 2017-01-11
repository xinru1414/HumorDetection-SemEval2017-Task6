import sys, os
import csv
import re

# read in all files from train_dir/train_data
root_path = 'train_dir/train_data'
outfile = 'plain.txt'


with open(outfile, 'w') as o:
	for filename in os.listdir(root_path):
		fullpath = os.path.join(root_path, filename)
		# read in file line by line
		with open(fullpath,'r') as tsvin:
			tsvin = csv.reader(tsvin, delimiter='\t')
			for row in tsvin:
				# getting rid of links
				row = re.sub(r'https?:\/\/.*', '', str(row[1]), flags=re.MULTILINE)
				o.write(row + '\n')