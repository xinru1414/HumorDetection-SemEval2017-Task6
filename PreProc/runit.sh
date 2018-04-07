echo 'Pre processing tweets for training data'
python2 pre_tweet.py ../NgramLM/mydata/lm_train_dir/lm_train_data ../NgramLM/mydata/lm_train_dir/lm_train_data_pre
echo 'Pre processing tweets for evaluation data'
python2 pre_tweet.py ../data/evaluation_dir/evaluation_data ../data/evaluation_dir/evaluation_data_pre
echo 'Pre processing news training data'
python3 pre_news.py ../data/news_dir/various_size_news/1MBnew.txt ../data/news_dir/various_size_news/new1MB.txt