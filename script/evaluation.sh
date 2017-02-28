echo 'Evaluating Task A (with news training data)'
python code/TaskA_Eval/TaskA_Eval_Script.py mydata/lm_news_result/A_lm/ data/gold_data/
echo 'Evaluating Task B (with news training data)'
python code/TaskB_Eval/TaskB_Eval_Script.py mydata/lm_news_result/B_lm/ data/gold_data/
echo 'Evaluating Task A (with tweets training data)'
python code/TaskA_Eval/TaskA_Eval_Script.py mydata/lm_train_result/A_lm/ data/gold_data/
echo 'Evaluating Task B (with tweets training data)'
python code/TaskB_Eval/TaskB_Eval_Script.py mydata/lm_train_result/B_lm/ data/gold_data/
