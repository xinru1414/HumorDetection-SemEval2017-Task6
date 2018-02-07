'''
Feb 2018
Deep Learning method for Humor Detection
Xinru Yan

This file includes the set up for the deep learning model
and commone methods used for the project
'''

import string

START_TOKEN = "\x00"
UNK_TOKEN = "\x01"
SPACE = " "
STEP = 3
# vocab size!
chars = list(string.ascii_lowercase+string.digits+string.punctuation)+[UNK_TOKEN, SPACE, START_TOKEN]
CHAR_COUNT = len(chars)
MAXLEN = 40
LSTM_BATCH_SIZE = 128
char_indices = dict((c, i) for i, c in enumerate(chars))

def pad(tweet, start_token=START_TOKEN):
    """
    helper function to pad the training and testing data in order to get the probabilities for the start of the sentence!
    """
    return (start_token*MAXLEN) + tweet

def text2ints(text):
    """

    :param text: string
    :return: return strings to integers
    """
    text_ins = []
    for char in text:
        if char not in chars:
            char = UNK_TOKEN
        text_ins += [char_indices[char]]
    return text_ins

def get_prob(l):
    """
    helper function to get the probability for each tweet
    """
    sp = 1
    for i in range(len(l)):
        sp *= l[i]
    return sp