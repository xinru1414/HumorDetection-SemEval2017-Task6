# This directory contains all source code for the system stage 2 (Deep Learning Lanague Model)
## config.py
system configuration

Vocab size: 71

Number of LSTM units: 128

Input sequence length: 40 
## pre_process.py
preprocess training data
## train_model.py
train the language model

Model architecture: CharEmbedding + LSTM + Dropout + Dense

Batch size: 16384
## score.py
score testing data, get results ready for the evaluation
## test_score.py
a simple program for testing the learnt language model
