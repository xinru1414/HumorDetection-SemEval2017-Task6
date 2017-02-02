# SemEval 2017 Task 6 "#HashtagWars: Learning a sense of humor"
# Jan 2017
# Author: Xinru Yan University of Minnesota Duluth yanxx418@d.umn.edu

# Overview
# This program is for Task_B. It produces a ranking of tweets from funniest to least funny given an input file of tweets for a specific hashtag file. To be more specific, it takes in the results for each hashtag file from beets.py and for each hashtag file it outputs a file that contain tweet ids ranked in decreasing order according to how funny they are. The output file format meets the Evaluation criteria, showed as follows:
#	<winning tweet_id>
#	<top10 but not winning tweet_id>
#	...
#	<top10 but not winning tweet_id>
#	<not in top10 tweet_id>
#	...
#	<not in top10 tweet_id>

# Language: Python 2.7
# Command line example:
#	python cilantro_b.py lm_train_result/lm_score/
# Output file example: #BadInventions.tsv 
#	651782900413792257
#	651787332107022336
#	651777234198495232
#	651602018176364544


##### Program starts here #####
import os, sys
import csv

# do not read hidden files in the folder
def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

# input file folder. Change the path to your own path
root_path = sys.argv[1]

for filename in listdir_nohidden(root_path):
	fullpath = os.path.join(root_path, filename)
	if fullpath.endswith(".tsv"):
		outfile = fullpath.replace(".tsv", "") + '_PREDICT.tsv'
		outfile = outfile.replace("lm_score", "B_lm")
	# print(outfile)
	# read in file l
	with open(fullpath,'r') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		# sort the tweet based on the LM score they get
		sortedlist = sorted(tsvin, key=lambda row: float(row[2]), reverse=True)
		with open(outfile, 'w') as o:
			#o.write('\n'.join(map(str,sortedlist)))
			for i in range(len(sortedlist)):
				# real ouput
				o.write(sortedlist[i][0] + "\n")
				# experiments
				#o.write(sortedlist[i][0] + "\t" + sortedlist[i][1] + "\t" + sortedlist[i][2] + "\n")
##### Program ends here #####