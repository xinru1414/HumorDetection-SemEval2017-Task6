from __future__ import print_function, division

import sys
import os
import itertools

if len(sys.argv) != 3:
    print('Usage:', __file__, '<prediction_dir> <gold_dir>')
    print(' ', 'The files in the <prediction_dir> should be named like their corresponding data files, but with _PREDICT prior to the .tsv extension')
    print('  ', 'For example, Hahstag_File.tsv should be named Hashtag_File_PREDICT.tsv')
    print(' ', 'The files in the <prediction_dir> should be formatted as follows: ')
    print('  ', '<tweet1_id>\\t<tweet2_id>\\t<prediction>')
    print('  ', 'where <prediction> is 1 if the first tweets is funnier and 0 otherwise')
    print(' ', 'The files in the <gold_dir> should be files formatted as have been released in train/trail data files')
    sys.exit(1)

predict_dir = sys.argv[1]
gold_dir = sys.argv[2]

predict_files = os.listdir(predict_dir)
gold_files = os.listdir(gold_dir)
predict_files.sort()
gold_files.sort()

error_count = 0.
pred_count = 0.
for pf, gf in zip(predict_files, gold_files):
    gf_path = os.path.join(gold_dir, gf)
    win_list = []
    top10_list = []
    nont10_list = []
    tweets_lists = [nont10_list, top10_list, win_list]
    for line in open(gf_path).readlines():
        t_id, t_text, t_label = line.strip().split('\t')
        tweets_lists[int(t_label)].append(t_id)
    pair_dict = {}
    for list1, list2 in itertools.combinations(tweets_lists, 2):
        for t1, t2 in itertools.product(list1, list2):
            pair_dict[(t1, t2)] = 0
            pair_dict[(t2, t1)] = 1
    pf_path = os.path.join(predict_dir, pf)
    for line in open(pf_path).readlines():
        t1_id, t2_id, pred = line.strip().split('\t')
        key = (t1_id, t2_id)
        if key in pair_dict:
            gold_val = pair_dict[key]
            pred_count += 1
            error_count += abs(int(pred) - gold_val)

accuracy = 1 - (error_count / pred_count)
print('evaluation accuracy is:', accuracy)
# print error_count
