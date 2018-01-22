# This folder contains the stage two method (Char-LSTM LM) for Humor detection
python version: python3.5
## Preprocess 
Pre-process training data (tweets or news) into npz foramt and put pre-processed data into the npz_files folder
For example:
```
python3 durian/pre_process.py ~/HumorDetection-SemEval2017Task6/mydata/plain.txt durian/npz_files/tweets_npfile.npz
```
## Train Language model 
Train LM on the pre-processed npz file, put the model into models folder:
For example:
```
python3 durian/train_model.py durian/npz_files/tweets_npfile.npz 128 20 models/model_tweets.h5
```
notice here that the model set up is: 128 batch size, 20 epochs
## Score tweets
Score testing data, give each tweet a probability and put results into evaluation_results_tweets folder
For example:
```
python3 durian/score.py ~/HumorDetection-SemEval2017Task6/data/evaluation_dir/evaluation_data ~/HumorDetection/durian/evaluation_results_tweets models/model_tweets.h5
```
Note that steps below are similar to stage one
## Evaluation
python version: python2.7
### Task_A:
#### Getting results ready for the evaluation script:
```
python durian/evaluation_a.py evaluation_results_tweets/ tweets
```
#### Evaluation
```
python ~/HumorDetection-SemEval2017Task6/code/TaskA_Eval/TaskA_Eval_Script.py durian/evaluation_A_dl_lm data/gold_data/
```
### Task_B:
TODO

## What's already here that are actually useful:
### Folders:
- evaluation_A_dl_lm: final evaluation results for stage two
- evaluation_results_news: raw results from news LM
- evaluation_results_tweets: raw results form tweet LM
- models: trained models
  - model_10.h5 is the model trained on 2010 news data
  - model_tweets.h5 is the model trainded on tweets data (20 epochs)
  - model_tweets_2.h5 is the model trainded on tweets data (1 epoch)
- npz_files: pre-processed data
### Programs:
- config.py: configuration of the system
- pre_process.py: pre-processing data
- train_model.py: train Char-LSTM LM
- score.py: score testing tweet
- evaluation_a.py: getting results ready for evaluation (in python2.7)

