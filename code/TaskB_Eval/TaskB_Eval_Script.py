from __future__ import print_function, division

import sys
import os

if len(sys.argv) != 3:
    print('Usage:', __file__, '<prediction_dir> <gold_dir>')
    print(' ', 'The files in the <prediction_dir> should be named like their corresponding data files, but with _PREDICT prior to the .tsv extension')
    print('  ', 'For example, Hahstag_File.tsv should be named Hashtag_File_PREDICT.tsv')
    print(' ', 'The files in the <prediction_dir> should contain tweet ids ranked in decreasing order of funniness as follows:')
    print('  ', '<winning tweet_id>')
    print('  ', '<top10 but not winning tweet_id>')
    print('  ', '...')
    print('  ', '<top10 but not winning tweet_id>')
    print('  ', '<not in top10 tweet_id>')
    print('  ', '...')
    print('  ', '<not in top10 tweet_id>')
    print(' ', 'The files in the <gold_dir> should be files formatted as have been released in train/trail data files')
    sys.exit(1)


predict_dir = sys.argv[1]
gold_dir = sys.argv[2]

def get_f1(prec, recall):
    if prec == 0 or recall == 0:
        return 0.0
    return 2*prec*recall / (prec+recall)

predict_files = os.listdir(predict_dir)
gold_files = os.listdir(gold_dir)
predict_files.sort()
gold_files.sort()


file_count = 0.
f1_sum = 0.
tweet_count = 0.
error = 0.
for pf, gf in zip(predict_files, gold_files):
    file_count += 1
    ht_tweet_count = 0.
    error_count = 0.
    gf_path = os.path.join(gold_dir, gf)
    label_dict = {}
    for line in open(gf_path).readlines():
        t_id, t_text, t_label = line.strip().split('\t')
        label_dict[t_id] = int(t_label)
    pf_path = os.path.join(predict_dir, pf)
    prec_raw = 10
    recall_raw = 10
    for tweet_ranking, line in enumerate(open(pf_path).readlines()):
        ht_tweet_count += 1
        t_id = line.strip()
        if tweet_ranking == 0:
            pred = 2
            fpred = 1
        elif tweet_ranking < 10:
            pred = 1
            fpred = 1
        else:
            pred = 0
            fpred = 0

        if t_id in label_dict:
            gold_val = label_dict[t_id]
            if gold_val >= 1:
                fgold = 1
            else:
                fgold = 0
            error_count += abs(pred - gold_val)
            if fpred == 1:
                prec_raw -= abs(fpred - fgold)
            if fgold == 1:
                recall_raw -= abs(fpred - fgold)
        else:  # this shouldn't happen
            print('error, following tweet not found:', t_id, pf)
    tweet_count += ht_tweet_count
    f1_sum += get_f1( prec_raw / 10 , recall_raw / 10 )
    error += ht_tweet_count * error_count / 22

print('evaluation distance is:', error/tweet_count)
print('average f1 score for predicting top 10 tweets:', f1_sum / file_count)
