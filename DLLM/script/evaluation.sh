echo 'Evaluating Task A (with news training data)'
python ../../Evaluation/cilantro_a.py ../../DLLM/mydata/evaluation_results_news news dl
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/A_lm ../../data/gold_data
echo 'Evaluating Task B (with news training data)'
python ../../Evaluation/cilantro_b.py ../../DLLM/mydata/evaluation_results_news news dl
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/B_lm ../../data/gold_data