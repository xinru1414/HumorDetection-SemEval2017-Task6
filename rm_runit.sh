# This script sets baseline for both tasks.

echo 'baseline for task A'
python src/random_gen_a.py mydata/lm_train_result/lm_score/
echo 'baseline for task B'
python src/random_gen_b.py mydata/lm_train_result/lm_score