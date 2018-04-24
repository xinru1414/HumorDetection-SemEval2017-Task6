echo 'DL Results 10mb 3Layer WithoutNormalization'
echo 'Evaluating Task A (with news training data)'
python ../../Evaluation/cilantro_a.py ../../DLLM/mydata/evaluation_results_news news dl
python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/A_lm ../../data/gold_data
echo 'Evaluating Task B (with news training data)'
python ../../Evaluation/cilantro_b.py ../../DLLM/mydata/evaluation_results_news news dl
python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/B_lm ../../data/gold_data

echo 'With Norm'
cp -R ../../DLLM/mydata/evaluation_results_news ../../DLLM/mydata/WithNorm/10mb
cp -R ../../DLLM/mydata/A_lm ../../DLLM/mydata/WithNorm/10mb
cp -R ../../DLLM/mydata/B_lm ../../DLLM/mydata/WithNorm/10mb

echo '\n'
echo 'Copying A files into single dirs'
cp ../../DLLM/mydata/WithNorm/10mb/A_lm/Bad_Job_In_5_Words_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/A_S/BJ/Bad_Job_In_5_Words_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/A_lm/Break_Up_In_5_Words_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/A_S/BU/Break_Up_In_5_Words_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/A_lm/Broadway_A_Celeb_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/A_S/BA/Broadway_A_Celeb_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/A_lm/Cereal_Songs_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/A_S/CS/Cereal_Songs_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/A_lm/Modern_Shakespeare_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/A_S/MS/Modern_Shakespeare_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/A_lm/Ruin_A_Christmas_Movie_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/A_S/RA/Ruin_A_Christmas_Movie_PREDICT.tsv
echo 'Results per file for Subtask A'
echo 'Bad_Job_In_5_Words'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/A_S/BJ ../../data/BJ
echo 'Break_Up_In_5_Words'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/A_S/BU ../../data/BU
echo 'Broadway_A_Celeb'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/A_S/BA ../../data/BA
echo 'Cereal_Songs'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/A_S/CS ../../data/CS
echo 'Modern_Shakespeare'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/A_S/MS ../../data/MS
echo 'Ruin_A_Christmas_Movie'
python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/A_S/RA ../../data/RA
echo '\n'
echo 'Copying B files into single dirs'
cp ../../DLLM/mydata/WithNorm/10mb/B_lm/Bad_Job_In_5_Words_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/B_S/BJ/Bad_Job_In_5_Words_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/B_lm/Break_Up_In_5_Words_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/B_S/BU/Break_Up_In_5_Words_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/B_lm/Broadway_A_Celeb_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/B_S/BA/Broadway_A_Celeb_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/B_lm/Cereal_Songs_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/B_S/CS/Cereal_Songs_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/B_lm/Modern_Shakespeare_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/B_S/MS/Modern_Shakespeare_PREDICT.tsv
cp ../../DLLM/mydata/WithNorm/10mb/B_lm/Ruin_A_Christmas_Movie_PREDICT.tsv ../../DLLM/mydata/WithNorm/10mb/B_S/RA/Ruin_A_Christmas_Movie_PREDICT.tsv
echo 'Restuls per file for Subtask B'
echo 'Bad_Job_In_5_Words'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/B_S/BJ ../../data/BJ
echo 'Break_Up_In_5_Words'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/B_S/BU ../../data/BU
echo 'Broadway_A_Celeb'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/B_S/BA ../../data/BA
echo 'Cereal_Songs'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/B_S/CS ../../data/CS
echo 'Modern_Shakespeare'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/B_S/MS ../../data/MS
echo 'Ruin_A_Christmas_Movie'
python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/WithNorm/10mb/B_S/RA ../../data/RA
# echo '\n'
# echo 'DL Results 10mb 3Layer WithoutNormalization'
# echo 'Evaluating Task A (with news training data)'
# python ../../Evaluation/cilantro_a.py ../../DLLM/mydata/evaluation_results_news news dl
# python ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/A_lm ../../data/gold_data
# echo 'Evaluating Task B (with news training data)'
# python ../../Evaluation/cilantro_b.py ../../DLLM/mydata/evaluation_results_news news dl
# python ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/B_lm ../../data/gold_data

# echo 'No Norm'
# cp -R ../../DLLM/mydata/evaluation_results_news ../../DLLM/mydata/NoNorm/10mb
# cp -R ../../DLLM/mydata/A_lm ../../DLLM/mydata/NoNorm/10mb
# cp -R ../../DLLM/mydata/B_lm ../../DLLM/mydata/NoNorm/10mb

# echo '\n'
# echo 'Copying A files into single dirs'
# cp ../../DLLM/mydata/NoNorm/10mb/A_lm/Bad_Job_In_5_Words_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/A_S/BJ/Bad_Job_In_5_Words_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/A_lm/Break_Up_In_5_Words_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/A_S/BU/Break_Up_In_5_Words_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/A_lm/Broadway_A_Celeb_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/A_S/BA/Broadway_A_Celeb_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/A_lm/Cereal_Songs_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/A_S/CS/Cereal_Songs_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/A_lm/Modern_Shakespeare_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/A_S/MS/Modern_Shakespeare_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/A_lm/Ruin_A_Christmas_Movie_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/A_S/RA/Ruin_A_Christmas_Movie_PREDICT.tsv
# echo 'Results per file for Subtask A'
# echo 'Bad_Job_In_5_Words'
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/A_S/BJ ../../data/BJ
# echo 'Break_Up_In_5_Words'
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/A_S/BU ../../data/BU
# echo 'Broadway_A_Celeb'
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/A_S/BA ../../data/BA
# echo 'Cereal_Songs'
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/A_S/CS ../../data/CS
# echo 'Modern_Shakespeare'
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/A_S/MS ../../data/MS
# echo 'Ruin_A_Christmas_Movie'
# python2 ../../Evaluation/TaskA_Eval/TaskA_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/A_S/RA ../../data/RA
# echo '\n'
# echo 'Copying B files into single dirs'
# cp ../../DLLM/mydata/NoNorm/10mb/B_lm/Bad_Job_In_5_Words_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/B_S/BJ/Bad_Job_In_5_Words_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/B_lm/Break_Up_In_5_Words_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/B_S/BU/Break_Up_In_5_Words_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/B_lm/Broadway_A_Celeb_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/B_S/BA/Broadway_A_Celeb_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/B_lm/Cereal_Songs_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/B_S/CS/Cereal_Songs_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/B_lm/Modern_Shakespeare_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/B_S/MS/Modern_Shakespeare_PREDICT.tsv
# cp ../../DLLM/mydata/NoNorm/10mb/B_lm/Ruin_A_Christmas_Movie_PREDICT.tsv ../../DLLM/mydata/NoNorm/10mb/B_S/RA/Ruin_A_Christmas_Movie_PREDICT.tsv
# echo 'Restuls per file for Subtask B'
# echo 'Bad_Job_In_5_Words'
# python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/B_S/BJ ../../data/BJ
# echo 'Break_Up_In_5_Words'
# python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/B_S/BU ../../data/BU
# echo 'Broadway_A_Celeb'
# python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/B_S/BA ../../data/BA
# echo 'Cereal_Songs'
# python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/B_S/CS ../../data/CS
# echo 'Modern_Shakespeare'
# python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/B_S/MS ../../data/MS
# echo 'Ruin_A_Christmas_Movie'
# python2 ../../Evaluation/TaskB_Eval/TaskB_Eval_Script.py ../../DLLM/mydata/NoNorm/10mb/B_S/RA ../../data/RA
# echo '\n'