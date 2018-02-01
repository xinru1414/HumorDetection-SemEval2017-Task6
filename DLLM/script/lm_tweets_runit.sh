echo 'Getting training data ready'
python3 ../src/pre_process.py ../../NgramLM/mydata/plain.txt ../mydata/npz_files/tweets
echo 'Training languge model'
python3 ../src/train_model.py ../mydata/npz_files/tweets 128 20 ../mydata/models/model_tweets_new.h5 > ../mydata/train_log/log_tweets_new_train.txt
echo 'Getting language model scores'
python3 ../src/score.py ../../data/evaluation_dir/evaluation_data ../mydata/evaluation_results_tweets_new ../mydata/models/model_tweets_new.h5
echo 'Getting result for task a'
python ../../Evaluation/cilantro_a.py ../mydata/evaluation_results_tweets_new tweets dl
echo 'Getting result for task b'
python ../../Evaluation/cilantro_b.py ../mydata/evaluation_results_tweets_new tweets dl