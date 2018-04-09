echo '1000line'
echo 'PreProcessing Training data'
python3 ../../PreProc/pre_news.py ../../data/news_dir/various_size_news/1000line.txt ../../data/news_dir/various_size_news/new1000line.txt
echo 'PreProcessing Evaluation data'
python3 ../../PreProc/pre_tweets.py ../../data/evaluation_dir/evaluation_data ../../data/evaluation_dir/evaluation_data_pre
echo 'PreProcessing data is done'
echo 'Now we train languge model'
../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ../../data/news_dir/various_size_news/new1000line.txt > ../mydata/1000line.arpa
echo 'Getting language model scores'
python2 ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/1000line.arpa
echo 'Evaluating Task A (with 1000line training data)'
python2 ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
echo 'Evaluating Task B (with 1000line training data)'
python2 ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
# echo '1MB'
# pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/1MB.arpa
# python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
# python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
# echo '10MB'
# pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/10.arpa
# python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
# python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
# echo '25MB'
# pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/25.arpa
# python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
# python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
# echo '50MB'
# pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/50.arpa
# python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
# python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
# echo '200MB'
# pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/200.arpa
# python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
# python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
# echo '500MB'
# pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/500.arpa
# python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
# python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
# echo '1GB'
# pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/1.arpa
# python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
# python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
# python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data