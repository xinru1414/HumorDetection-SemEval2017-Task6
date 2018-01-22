"""
This program preprocesses each directory of testing tweets
"""
import sys, os
import csv
import re
from keras.models import load_model
import numpy as np
import preprocessor as p
from config import *

# do not read hidden files in the folder
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def get_sentence_prob(sentence):
    """
    helper function to get the probabilities and keep things moving to the next
    """
    seed = sentence[:MAXLEN]
    assert len(seed) == MAXLEN
    sent_preds = []

    for i in range(len(sentence) - MAXLEN):
        x = np.zeros((1, MAXLEN), dtype=np.int8)
        for char_index, char in enumerate(seed):
            x[0, char_index] = char

        preds = model.predict(x, verbose=0)[0]
        sent_preds += [preds[sentence[MAXLEN + i]]]
        # keep it moving to the next
        seed = sentence[i:MAXLEN + i]
    return sent_preds


# input file path. Change the path to your own path
root_path = sys.argv[1]
# output file path. Change the path to your own path
result_path = sys.argv[2]
# set up news data or tweets data
# data = sys.argv[3]

# the training corpus
FILENAME = sys.argv[3]

# load the Language Model trained on the trainig data.
# text.arpa for funny tweets
# LM = "mydata/text.arpa"
# text_un.arpa for news data
model = load_model(FILENAME)
# if data == "tweets":
# 	LM = "mydata/text.arpa"
# else:
# 	LM = "mydata/text_un.arpa"
#
# model = kenlm.Model(LM)

# read in the file
for filename in listdir_nohidden(root_path):
    fullpath = os.path.join(root_path, filename)
    if filename.endswith(".tsv"):
        filename = filename.replace(".tsv", "")
    outfilefullpath = os.path.join(result_path, filename)
    # name the output file as the same as input file
    outfile = outfilefullpath + '.tsv'
    with open(fullpath, 'r') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
        with open(outfile, 'w') as tsvout:
            writer = csv.writer(tsvout, delimiter='\t')
            for row in tsvin:
                # raw tweet (without urls)
                rt = p.clean(str(row[1]).lower())
                #rt = re.sub(r'https?:\/\/.*', '', str(row[1]), flags=re.MULTILINE)
                #rt = rt.lower()
                #rt = re.sub(r'@midnight', '', str(row[1]), flags=re.MULTILINE)
                rt = text2ints(pad(rt))
                # print(rt, get_prob(get_sentence_prob(rt)))
                # print(rt)
                # score based on the language model for each tweet
                writer.writerow([row[0], row[1], get_prob(get_sentence_prob(rt)), get_sentence_prob(rt)])
                #writer.writerow([row[0], row[1], get_prob(get_sentence_prob(rt))])
