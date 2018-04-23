echo 'Trigram Lowercase + No @ + T + Keep #'
echo 'PreProcessing Evaluation data'
python3 ../../PreProc/pre_tweet.py ../mydata/lm_train_dir/lm_train_data/ ../mydata/lm_train_dir/lm_train_data_pre/

echo '100K'
../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Developer/Thesis/SemEval2017/Humor/AD/new100KL.txt > ../mydata/100KL.arpa
python2 ../src/beets.py ../mydata/lm_train_dir/lm_train_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/100KL.arpa
python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../mydata/lm_train_dir/lm_train_data



# echo '1MB'
# ../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Developer/Thesis/SemEval2017/Humor/AD/new1MBL.txt > ../mydata/1MBL.arpa
# python2 ../src/beets.py ../mydata/lm_train_dir/lm_train_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/1MBL.arpa
# python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../mydata/lm_train_dir/lm_train_data


# echo '10MB'
# ../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Developer/Thesis/SemEval2017/Humor/AD/new10MBL.txt > ../mydata/10MBL.arpa
# python2 ../src/beets.py ../mydata/lm_train_dir/lm_train_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/10MBL.arpa
# python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../mydata/lm_train_dir/lm_train_data


# echo '25MB'
# ../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Developer/Thesis/SemEval2017/Humor/AD/new25MBL.txt > ../mydata/25MBL.arpa
# python2 ../src/beets.py ../mydata/lm_train_dir/lm_train_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/25MBL.arpa
# python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../mydata/lm_train_dir/lm_train_data



# echo '50MB'
# ../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Developer/Thesis/SemEval2017/Humor/AD/new50MBL.txt > ../mydata/50MBL.arpa
# python2 ../src/beets.py ../mydata/lm_train_dir/lm_train_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/50MBL.arpa
# python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../mydata/lm_train_dir/lm_train_data



# echo '200MB'
# ../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Developer/Thesis/SemEval2017/Humor/AD/new200MBL.txt > ../mydata/200MBL.arpa
# python2 ../src/beets.py ../mydata/lm_train_dir/lm_train_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/200MBL.arpa
# python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../mydata/lm_train_dir/lm_train_data



# echo '500MB'
# ../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Developer/Thesis/SemEval2017/Humor/AD/new500MBL.txt > ../mydata/500MBL.arpa
# python2 ../src/beets.py ../mydata/lm_train_dir/lm_train_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/500MBL.arpa
# python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../mydata/lm_train_dir/lm_train_data



# echo '1GB'
# ../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Developer/Thesis/SemEval2017/Humor/AD/new1GBL.txt > ../mydata/1GBL.arpa
# python2 ../src/beets.py ../mydata/lm_train_dir/lm_train_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/1GBL.arpa
# python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../mydata/lm_train_dir/lm_train_data

