echo 'Evaluating Task A (with news training data)'
#TODO
echo 'Evaluating Task B (with news training data)'
#TODO
echo 'Evaluating Task A (with tweets training data)'
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../mydata/evaluation_A_lm ../../data/gold_data
echo 'Evaluating Task B (with tweets training data)'
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../mydata/evaluation_B_lm ../../data/gold_data