'''
Feb 2018
Deep Learning method for Humor Detection
Xinru Yan

This program trains the char-based LSTM language model

Note that it uses fit_generator to avoid loading the entire dataset at once
since one of the training dataset is relatively large

Usage:
    python3 train_model.py TRAINING_DATA_INPUT_FOLDER BATCH_SIZE EPOCH_NUMBER SAVED_MODEL_NAME
    e.g.:
    python3 train_model.py ../mydata/npz_files/tweets 128 20 ../mydata/models/model_tweets_new.h5
'''
from __future__ import print_function, division
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from keras.layers import LSTM, Embedding, Dropout, Conv1D, MaxPooling1D
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
import keras.backend as K
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
#import click
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

# def perplexity(y_true, y_pred):
#     cross_entropy = K.categorical_crossentropy(y_true, y_pred)
#     perplexity = K.pow(2.0, K.mean(-K.log2(y_pred)))
#     return perplexity
#
def cross_entropy(y_true, y_pred):
    cross_entropy = K.categorical_crossentropy(y_true, y_pred)
    # perplexity = K.pow(2.0, cross_entropy)
    return cross_entropy

# model setup
def build_model(maxlen=MAXLEN, lstm_batch_size=LSTM_BATCH_SIZE, char_count=CHAR_COUNT, em=EM, lr=LR):
    model = Sequential()
    model.add(Embedding(char_count, em, input_length=maxlen))
    # model.add(LSTM(LSTM_BATCH_SIZE, input_shape=(MAXLEN, CHAR_COUNT)))
    #model.add(Dropout(0.5))
    #model.add(Conv1D(filters=128, kernel_size=5, activation='relu', padding='valid'))
    #model.add(MaxPooling1D(pool_size=5))
    #model.add(LSTM(lstm_batch_size, return_sequences=True))
    model.add(LSTM(lstm_batch_size))
    #model.add(Dropout(0.3))
    model.add(Dense(CHAR_COUNT, activation="softmax"))
    #model.add(Dropout(0.5))
    # model.add(Activation('softmax'))

    optimizer = RMSprop(lr=LR)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['categorical_crossentropy'])


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

    @property
    def steps_per_epoch(self):
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
    model_name = sys.argv[4]
    pic_name = sys.argv[5]

    train_data = DataLoader(np_dir+"/train", batch_size, MAXLEN)
    val_data = DataLoader(np_dir+"/val", batch_size, MAXLEN)

    model = build_model()

    # checkpoint
    filepath = model_name
    checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

    callbacks_list = [checkpoint]

    print(model.summary())
    #model.fit_generator(train_data, steps_per_epoch=train_data.steps_per_epoch, epochs=epochs, callbacks=callbacks_list, workers=10, use_multiprocessing=True, verbose=1, validation_data=val_data, validation_steps=val_data.steps_per_epoch)
    #model.fit_generator(data, steps_per_epoch=data.steps_per_epoch, epochs=epochs, callbacks=callbacks_list)
    history = model.fit_generator(train_data, steps_per_epoch=train_data.steps_per_epoch, epochs=epochs, callbacks=callbacks_list,
                        workers=10, verbose=1, validation_data=val_data,
                        validation_steps=val_data.steps_per_epoch)
    # list all data in history
    print(history.history.keys())
    # summarize history for cross_en
    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.plot(history.history['cross_entropy'])
    plt.plot(history.history['val_cross_entropy'])
    plt.title('model crossentropy')
    plt.ylabel('crossentropy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.savefig(pic_name)
    # summarize history for loss
    # plt.plot(history.history['perplexity'])
    # plt.plot(history.history['val_perplexity'])
    # plt.title('LM perplexity')
    # plt.ylabel('perplexity')
    # plt.xlabel('epoch')
    # plt.legend(['train', 'val'], loc='upper left')
    # # plt.show()
    # plt.savefig('perplexity.png')
    # save the model to file
    #model.save(model_name)

if __name__ == '__main__':
    main()
