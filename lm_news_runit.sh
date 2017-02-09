echo 'Getting language model scores'
python src/beets.py data/evaluation_dir/evaluation_data/ mydata/lm_news_result/lm_score/
echo 'Getting result for task a'
python src/cilantro_a.py mydata/lm_news_result/lm_score/
echo 'Getting result for task b'
python src/cilantro_b.py mydata/lm_news_result/lm_score/