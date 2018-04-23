echo 'Trigram Lowercase + No @ + T + Keep #'
echo 'PreProcessing Evaluation data'
python3 ../../PreProc/pre_tweet.py ../../data/evaluation_dir/evaluation_data ../../data/evaluation_dir/evaluation_data_pre
echo 'PreProcessing Training data'
#python3 ../../PreProc/pre_news.py ~/Documents/deu_news_2009_100K/100Kxyzabc.txt ~/Documents/deu_news_2009_100K/xyzabc100K.txt

echo 'xyzcbc'
../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ~/Documents/deu_news_2009_100K/xyzabc100K.txt > ../mydata/xyzabc.arpa
python2 ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/xyzabc.arpa
python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
python2 ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data

cp -R ../mydata/lm_news_result/lm_score ../mydata/xyzabc/
cp -R ../mydata/lm_news_result/A_lm ../mydata/xyzabc/
cp -R ../mydata/lm_news_result/B_lm ../mydata/xyzabc/
cp -R ../mydata/lm_news_result/B_lm ../../Analysis/

echo '\n'
echo 'Copying A files into single dirs'
cp ../mydata/lm_news_result/A_lm/Bad_Job_In_5_Words_PREDICT.tsv ../mydata/lm_news_result/A_S/BJ/Bad_Job_In_5_Words_PREDICT.tsv
cp ../mydata/lm_news_result/A_lm/Break_Up_In_5_Words_PREDICT.tsv ../mydata/lm_news_result/A_S/BU/Break_Up_In_5_Words_PREDICT.tsv
cp ../mydata/lm_news_result/A_lm/Broadway_A_Celeb_PREDICT.tsv ../mydata/lm_news_result/A_S/BA/Broadway_A_Celeb_PREDICT.tsv
cp ../mydata/lm_news_result/A_lm/Cereal_Songs_PREDICT.tsv ../mydata/lm_news_result/A_S/CS/Cereal_Songs_PREDICT.tsv
cp ../mydata/lm_news_result/A_lm/Modern_Shakespeare_PREDICT.tsv ../mydata/lm_news_result/A_S/MS/Modern_Shakespeare_PREDICT.tsv
cp ../mydata/lm_news_result/A_lm/Ruin_A_Christmas_Movie_PREDICT.tsv ../mydata/lm_news_result/A_S/RA/Ruin_A_Christmas_Movie_PREDICT.tsv
echo 'Results per file for Subtask A'
echo 'Bad_Job_In_5_Words'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_S/BJ ../../data/BJ
echo 'Break_Up_In_5_Words'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_S/BU ../../data/BU
echo 'Broadway_A_Celeb'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_S/BA ../../data/BA
echo 'Cereal_Songs'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_S/CS ../../data/CS
echo 'Modern_Shakespeare'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_S/MS ../../data/MS
echo 'Ruin_A_Christmas_Movie'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_S/RA ../../data/RA
echo '\n'
echo 'Copying B files into single dirs'
cp ../mydata/lm_news_result/B_lm/Bad_Job_In_5_Words_PREDICT.tsv ../mydata/lm_news_result/B_S/BJ/Bad_Job_In_5_Words_PREDICT.tsv
cp ../mydata/lm_news_result/B_lm/Break_Up_In_5_Words_PREDICT.tsv ../mydata/lm_news_result/B_S/BU/Break_Up_In_5_Words_PREDICT.tsv
cp ../mydata/lm_news_result/B_lm/Broadway_A_Celeb_PREDICT.tsv ../mydata/lm_news_result/B_S/BA/Broadway_A_Celeb_PREDICT.tsv
cp ../mydata/lm_news_result/B_lm/Cereal_Songs_PREDICT.tsv ../mydata/lm_news_result/B_S/CS/Cereal_Songs_PREDICT.tsv
cp ../mydata/lm_news_result/B_lm/Modern_Shakespeare_PREDICT.tsv ../mydata/lm_news_result/B_S/MS/Modern_Shakespeare_PREDICT.tsv
cp ../mydata/lm_news_result/B_lm/Ruin_A_Christmas_Movie_PREDICT.tsv ../mydata/lm_news_result/B_S/RA/Ruin_A_Christmas_Movie_PREDICT.tsv
echo 'Restuls per file for Subtask B'
echo 'Bad_Job_In_5_Words'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_S/BJ ../../data/BJ
echo 'Break_Up_In_5_Words'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_S/BU ../../data/BU
echo 'Broadway_A_Celeb'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_S/BA ../../data/BA
echo 'Cereal_Songs'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_S/CS ../../data/CS
echo 'Modern_Shakespeare'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_S/MS ../../data/MS
echo 'Ruin_A_Christmas_Movie'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_S/RA ../../data/RA
echo '\n'