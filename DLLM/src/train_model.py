
from __future__ import print_function, division
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from keras.layers import LSTM, Embedding, Dropout
from keras.utils import to_categorical
from nltk.tokenize import TweetTokenizer
import numpy as np
import click
import sys
import os
from math import ceil
from config import *

# # load the pre_processed numpy file
# NPFILE = sys.argv[1]
# # set up the batch size
# GEN_BATCH_SIZE = int(sys.argv[2])
# # set up epochs
# EPOCHS = int(sys.argv[3])
# # model name and location
# MODEL_NAME = (sys.argv[4])
#
# #load the np file
# npzfile = np.load(NPFILE)
#
# sentences = npzfile['x']
# next_chars = npzfile['y']
# print("nb sequences", len(sentences))

# build the model: a single LSTM
def build_model(maxlen=MAXLEN, lstm_batch_size=LSTM_BATCH_SIZE, char_count=CHAR_COUNT):
    model = Sequential()
    model.add(Embedding(char_count, 128, input_length=maxlen))
    # model.add(LSTM(LSTM_BATCH_SIZE, input_shape=(MAXLEN, CHAR_COUNT)))
    model.add(LSTM(lstm_batch_size))
    model.add(Dropout(0.5))
    model.add(Dense(CHAR_COUNT, activation="softmax"))
    # model.add(Activation('softmax'))

    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model


class DataLoader(object):
    def __init__(self, np_dir, batch_size, max_len):
        self.np_dir = np_dir
        self.batch_size = batch_size
        self.max_len = max_len
        self.sentence_buffer = None
        self.next_char_buffer = None
        self.cur_npz_file = 0
        self.__get_npz_files()
        self.__get_data_count()

    def __get_npz_files(self):
        self.npz_files = os.listdir(self.np_dir)
        self.npz_files.pop(self.npz_files.index("data_count"))
        self.npz_files.sort()

    def __get_data_count(self):
        self.sentence_count = int(open("{}/data_count".format(self.np_dir), "r").read())

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def __len__(self):
        return int(ceil(self.sentence_count/self.batch_size))

    def get_more_sentences(self):
        if self.cur_npz_file >= len(self.npz_files):
            self.cur_npz_file = 0
        cur_npz_fn = self.npz_files[self.cur_npz_file]
        self.cur_npz_file += 1
        npz_file = np.load(os.path.join(self.np_dir, cur_npz_fn))
        if self.sentence_buffer is None:
            self.sentence_buffer = npz_file["x"]
            self.next_char_buffer = npz_file["y"]
        else:
            self.sentence_buffer = np.concatenate((self.sentence_buffer, npz_file["x"]))
            self.next_char_buffer = np.concatenate((self.next_char_buffer, npz_file["y"]))
        return len(npz_file["x"])

    def next(self):
        while self.sentence_buffer is None or len(self.sentence_buffer) <= self.batch_size:
            if self.get_more_sentences() == 0:
                break

        # if len(self.sentence_buffer) == 0:
        #     raise StopIteration()

        batch_sentences = self.sentence_buffer[:self.batch_size]
        batch_next_chars = self.next_char_buffer[:self.batch_size]
        self.sentence_buffer = self.sentence_buffer[self.batch_size:]
        self.next_char_buffer = self.next_char_buffer[self.batch_size:]

        batch_size = len(batch_sentences)
        assert len(batch_next_chars) == batch_size, "We have an issue! The number of new_chars doesn't match the number of sentences."

        batch_X = np.zeros((batch_size, self.max_len), dtype=np.int8)
        batch_y = np.zeros((batch_size,), dtype=np.int)
        for sent_index, sentence in enumerate(batch_sentences):
            batch_y[sent_index] = batch_next_chars[sent_index]
            for char_index, char in enumerate(sentence):
                batch_X[sent_index, char_index] = char

        # one hot encode here
        batch_y = to_categorical(batch_y, num_classes=CHAR_COUNT)

        return batch_X, batch_y


# @click.command()
# @click.argument('np_dir', type=click.Path(exists=True))
# @click.argument('batch_size')
# @click.argument('epochs', type=int)
# @click.argument('model_name')
def main():
    # np_dir, batch_size, epochs, model_name
    """Train a LM on preprocessed data."""
    np_dir = sys.argv[1]
    batch_size = int(sys.argv[2])
    epochs = int(sys.argv[3])
    model_name = (sys.argv[4])

    data = DataLoader(np_dir, batch_size, MAXLEN)

    model = build_model()
    model.fit_generator(data, steps_per_epoch=len(data), epochs=epochs)

    # save the model to file
    model.save(model_name)

if __name__ == '__main__':
    main()
