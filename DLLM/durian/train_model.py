from __future__ import print_function, division
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from keras.layers import LSTM, Embedding, Dropout
from keras.utils import to_categorical
from nltk.tokenize import TweetTokenizer
import numpy as np
import sys
from math import ceil
from config import *

# load the pre_processed numpy file
NPFILE = sys.argv[1]
# set up the batch size
GEN_BATCH_SIZE = int(sys.argv[2])
# set up epochs
EPOCHS = int(sys.argv[3])
# model name and location
MODEL_NAME = (sys.argv[4])

#load the np file
npzfile = np.load(NPFILE)

sentences = npzfile['x']
next_chars = npzfile['y']
print("nb sequences", len(sentences))


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
            # one_hot_encoding here
            batch_y = to_categorical(batch_y, num_classes=CHAR_COUNT)
            # print(len(batch_X[0]))
            #print(batch_X.max())
            yield batch_X, batch_y
            # random.shuffle(sentences)

# build the model: a single LSTM
def build_model(maxlen=MAXLEN, lstm_batch_size=LSTM_BATCH_SIZE, char_count=CHAR_COUNT, epochs=EPOCHS, gen_batch_size=GEN_BATCH_SIZE):
    model = Sequential()
    model.add(Embedding(char_count, 128, input_length=maxlen))
    # model.add(LSTM(LSTM_BATCH_SIZE, input_shape=(MAXLEN, CHAR_COUNT)))
    model.add(LSTM(lstm_batch_size))
    model.add(Dropout(0.5))
    model.add(Dense(CHAR_COUNT, activation="softmax"))
    # model.add(Activation('softmax'))

    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    batches = ceil(len(sentences)/gen_batch_size)

    # model.fit(X, y, batch_size=128, epochs=1)
    model.fit_generator(generator(gen_batch_size), steps_per_epoch=batches, epochs=epochs)

    # save the model to file
    model.save(MODEL_NAME)
    return model

build_model()


