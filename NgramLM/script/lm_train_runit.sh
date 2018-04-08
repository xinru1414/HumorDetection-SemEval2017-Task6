# This script runs experiments using language models with training data (aka the tweets data) from the SemEval task
echo 'Getting training data ready'
python2 ../src/avocado.py ../mydata/lm_train_dir/lm_train_data/ ../mydata/plain.txt
echo 'Training languge model'
../KenLM/kenlm-master/build/bin/lmplz -o 3 -S 70% < ../mydata/plain.txt > ../mydata/text.arpa
echo 'Getting language model scores'
pipenv run python ../src/beets.py ../../data/evaluation_dir/evaluation_data/ ../mydata/lm_train_result/lm_score/ ../mydata/text.arpa
echo 'Getting result for task a'
python ../../Evaluation/cilantro_a.py ../mydata/lm_train_result/lm_score/ tweets Ngram
echo 'Getting result for task b'
python ../../Evaluation/cilantro_b.py ../mydata/lm_train_result/lm_score/ tweets Ngram
echo 'Evaluating Task A (with tweets training data)'
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../mydata/lm_train_result/A_lm/ ../../data/gold_data/
echo 'Evaluating Task B (with tweets training data)'
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../mydata/lm_train_result/B_lm/ ../../data/gold_data/