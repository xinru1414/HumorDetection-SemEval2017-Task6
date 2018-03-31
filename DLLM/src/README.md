# This directory contains all source code for the system stage 2 (Deep Learning Lanague Model)
## config.py
system configuration

Vocab size: 71

Number of LSTM units: 128

Number of Embedding units: 10

Input sequence length: 40 

Learning rate: 0.001

## pre_process.py
preprocess training data
excusively for news, since we don't train tweets neural LM
## train_model.py
train the language model

Model architecture: CharEmbedding + LSTM + Dropout + Dense

Batch size: 16384
## score.py
score testing data, get results ready for the evaluation
score scheme is the same as Ngram (only get rid of links from tweets)
## test_score.py
a simple program for testing the learnt language model

##example of news pre_process:
Assume our input sequence length (MAX) is 10 (10 chars long)

We have a 9-char long sentence "love wins", start_token is P, STEP =3 (jump 3 chars at a time, see config.py)

PPPPPPPPPPlove wins (padded sentence)

input pair to neural nets:

X1			Y1

PPPPPPPPPP  l

X2			Y2

PPPPPPPlov  e

X3			Y3

PPPPlove w  i

...