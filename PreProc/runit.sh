echo 'Pre processing tweets for training data'
python2 pre_tweet.py ../NgramLM/mydata/lm_train_dir/lm_train_data ../NgramLM/mydata/lm_train_dir/lm_train_data_pre
echo 'Pre processing tweets for evaluation data'
python2 pre_tweet.py ../data/evaluation_dir/evaluation_data ../data/evaluation_dir/evaluation_data_pre
echo 'Pre processing news training data'
python3 pre_news.py ../data/news_dir/various_size_news/1MBnew.txt ../data/news_dir/various_size_news/new1MB.txt
python3 pre_news.py ~/Developer/Thesis/SemEval2017/Humor/AD/1MBnew.txt ~/Developer/Thesis/SemEval2017/Humor/AD/new1MB.txt
python3 pre_news.py ~/Developer/Thesis/SemEval2017/Humor/AD/10MBnew.txt ~/Developer/Thesis/SemEval2017/Humor/AD/new10MB.txt
python3 pre_news.py ~/Developer/Thesis/SemEval2017/Humor/AD/25MBnew.txt ~/Developer/Thesis/SemEval2017/Humor/AD/new25MB.txt
python3 pre_news.py ~/Developer/Thesis/SemEval2017/Humor/AD/50MBnew.txt ~/Developer/Thesis/SemEval2017/Humor/AD/new50MB.txt
python3 pre_news.py ~/Developer/Thesis/SemEval2017/Humor/AD/200MBnew.txt ~/Developer/Thesis/SemEval2017/Humor/AD/new200MB.txt
python3 pre_news.py ~/Developer/Thesis/SemEval2017/Humor/AD/500MBnew.txt ~/Developer/Thesis/SemEval2017/Humor/AD/new500MB.txt
python3 pre_news.py ~/Developer/Thesis/SemEval2017/Humor/AD/1GBnew.txt ~/Developer/Thesis/SemEval2017/Humor/AD/new1GB.txt
