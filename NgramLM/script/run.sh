echo '1MB'
pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/1MB.arpa
python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
echo '10MB'
pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/10.arpa
python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
echo '25MB'
pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/25.arpa
python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
echo '50MB'
pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/50.arpa
python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
echo '200MB'
pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/200.arpa
python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
echo '500MB'
pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/500.arpa
python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data
echo '1GB'
pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_news_result/lm_score/ ../mydata/1.arpa
python ../../Evaluation/cilantro_a.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../NgramLM/mydata/lm_news_result/A_lm ../../data/gold_data
python ../../Evaluation/cilantro_b.py ../mydata/lm_news_result/lm_score/ news Ngram
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../NgramLM/mydata/lm_news_result/B_lm ../../data/gold_data