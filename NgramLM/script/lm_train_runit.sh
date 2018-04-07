# This script runs experiments using language models with training data (aka the tweets data) from the SemEval task
echo 'Getting training data ready'
python ../src/avocado.py ../mydata/lm_train_dir/lm_train_data ../mydata/plain.txt
echo 'Training languge model'
../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ../mydata/plain.txt > ../mydata/text.arpa
echo 'Getting language model scores'
python ../src/beets.py data/evaluation_dir/evaluation_data_pre/ ../mydata/lm_train_result/lm_score/ tweets
echo 'Getting result for task a'
python ../src/cilantro_a.py ../mydata/lm_train_result/lm_score/ tweets
echo 'Getting result for task b'
python ../src/cilantro_b.py ../mydata/lm_train_result/lm_score/ tweets
