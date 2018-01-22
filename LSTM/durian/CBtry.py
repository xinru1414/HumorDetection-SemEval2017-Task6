from __future__ import print_function, division
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from keras.layers import LSTM, Embedding, Dropout
from keras.models import load_model
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from nltk.tokenize import TweetTokenizer
from nltk import FreqDist
import string
import random
import numpy as np
import sys
from math import ceil
import json
"""
How to run:
python CBtry.py TRAININGCORPUS_FILE_NAME
for example:
python CBtry.py kt.txt
"""

# the training corpus
FILENAME = sys.argv[1]
# output json file
OUT = sys.argv[2]
# taking 50 examples per pass
GEN_BATCH_SIZE = int(sys.argv[3])

# parameter setting
# how many characters for each snippet (length)
MAXLEN = 40
LSTM_BATCH_SIZE = 64
STEP = 3

# start token, unknown token and space
START_TOKEN = "\x00"  # using null byte because we are assuming that it does not appear in the corpus (This is double checked.)
UNK_TOKEN = "\x01"  # using \x01 byte to represent unknown char
SPACE = " "
# fixed size of vocab of the characterLSTMLM, 71 characters
chars = list(string.ascii_lowercase+string.digits+string.punctuation)+[UNK_TOKEN, SPACE, START_TOKEN]
CHAR_COUNT = len(chars)

def pad(tweet, start_token=START_TOKEN):
    """
    helper function to pad the training and testing data in order to get the probabilities for the start of the sentence!
    """
    return (start_token*MAXLEN) + tweet


def read_file(filename):
    """
    read in input file as lower_case text, get rid of new line and return text as string
    """
    text = []
    f = open(filename, "r", encoding = 'UTF-8')
    lines = f.readlines()
    for line in lines:
         text.append(pad(line.lower().replace("\n", " ")))
    return "".join(text)


print("Reading tweet file...")
# read in the file
text = read_file(FILENAME)
print('corpus length:', len(text))
#print(text)

print('total chars:', len(chars))
#char_indices(chars)
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

def text2ints(text):
    text_ins = []
    for char in text:
        if char not in chars:
            char = UNK_TOKEN
        text_ins += [char_indices[char]]
    return text_ins

#print(text)
text = text2ints(text)

# def save_text2ins(sequence):

#print(text2ints(text))

# preprocess the text in semi-redundant sequences of maxlen characters
sentences = []
next_chars = []
for i in range(0, len(text) - MAXLEN, STEP):
    sentences.append(text[i: i + MAXLEN])
    next_chars.append(text[i + MAXLEN])

print('nb sequences:', len(sentences))

#print(sentences)

def generator(preferred_batch_size):
    # setup variables
    batches = ceil(len(sentences)/preferred_batch_size)
    while True:
        for j in range(batches):
            batch = sentences[j*preferred_batch_size: (j+1)*preferred_batch_size]
            batch_next_chars = next_chars[j*preferred_batch_size: (j+1)*preferred_batch_size]
            batch_size = len(batch)
            batch_X = np.zeros((batch_size, MAXLEN), dtype=np.int8)
            batch_y = np.zeros((batch_size, ), dtype=np.int)
            for sent_index, sentence in enumerate(batch):
                batch_y[sent_index] = batch_next_chars[sent_index]
                for char_index, char in enumerate(sentence):
                    batch_X[sent_index, char_index] = char

            batch_y = to_categorical(batch_y)
            # print(len(batch_X[0]))
            #print(batch_X.max())
            yield batch_X, batch_y
            # random.shuffle(sentences)


# X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
# y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
# for i, sentence in enumerate(sentences):
#     for t, char in enumerate(sentence):
#         X[i, t, char_indices[char]] = 1
#     y[i, char_indices[next_chars[i]]] = 1
# print(len(sentences))
# print(len(X))

obj = {"maxlen": MAXLEN,
       "chars": chars,
       "start_token": START_TOKEN,
       "char_indices": char_indices}
json.dump(obj, open(OUT, "w"))


# build the model: a single LSTM
print('Build model...')
model = Sequential()
model.add(Embedding(CHAR_COUNT, 128, input_length=MAXLEN))
# model.add(LSTM(LSTM_BATCH_SIZE, input_shape=(MAXLEN, CHAR_COUNT)))
model.add(LSTM(LSTM_BATCH_SIZE))
model.add(Dropout(0.5))
model.add(Dense(CHAR_COUNT, activation="softmax"))
# model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

batches = ceil(len(sentences)/GEN_BATCH_SIZE)

# model.fit(X, y, batch_size=128, epochs=1)
model.fit_generator(generator(GEN_BATCH_SIZE), steps_per_epoch=batches, epochs=20)

# save the model to file
model.save('model.h5')

def get_sentence_prob(sentence):
    """
    helper function to get the probabilities and keep things moving to the next
    """
    seed = sentence[:MAXLEN]
    assert len(seed) == MAXLEN
    sent_preds = []

    for i in range(len(sentence)-MAXLEN):
        # Vectorization
        # x = np.zeros((1, MAXLEN, len(chars)))
        # for t, token in enumerate(seed):
        #     x[0, t, char_indices[token]] = 1
        x = np.zeros((1, MAXLEN), dtype=np.int8)
        for char_index, char in enumerate(seed):
            x[0, char_index] = char

        preds = model.predict(x, verbose=0)[0]
        sent_preds += [preds[sentence[MAXLEN + i]]]
        # keep it moving to the next
        seed = sentence[i:MAXLEN + i]
    return sent_preds

def get_prob(l):
    """
    helper funtion to get the probability for each tweet
    """
    sp = 1
    for i in range(len(l)):
        sp *= l[i]
    return sp

#output probabilities after each iteration
for iteration in range(1, 2):
    print()
    print('-' * 50)
    print('Iteration', iteration)
    # only 1 epoch for now!

    model = load_model('model.h5')
    # you get to see the probabilities. notice that padding of the testing data happens here
    print(pad("i am jim"))
    print(text2ints(pad("i am jim")))
    print(get_sentence_prob(text2ints(pad("i am jim"))))

    # print(get_sentence_prob(pad("jim i am")))
    # print(get_sentence_prob(pad("send que")))


print("\nThe final probability for sentences: ")
print("i am jim", get_prob(get_sentence_prob(text2ints(pad("i am jim")))))
# print("jim i am", get_prob(get_sentence_prob(pad("jim i am"))))
# print("send que", get_prob(get_sentence_prob(pad("send que"))))

