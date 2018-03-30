'''
Feb 2018
Deep Learning method for Humor Detection
Xinru Yan

This file includes the set up for the deep learning model
and commone methods used for the project
'''

import string
import math


START_TOKEN = "\x00"
UNK_TOKEN = "\x01"
SPACE = " "
STEP = 3
# vocab size!
chars = list(string.ascii_lowercase+string.digits+string.punctuation)+[UNK_TOKEN, SPACE, START_TOKEN]
#chars = ['\\', '„', '%', 'ÿ', '̂', ';', ' ', '?', ']', '¦', 'à', '\uf02c', '\u2028', '§', 'n', '+', ',', 'ì', 'g', '£', '♥', '¤', 'æ', 'q', '/', 'ï', '¨', 'j', '`', 'í', 'ä', '<', '̀', '™', 'k', 'õ', 'ﬀ', '¾', '´', '³', 'ŵ', '6', '5', 's', 'z', '«', 'ě', '\x9d', '€', 'c', 'ø', '¥', '*', '7', '2', '.', 'ˆ', 'h', '\uf021', 'ﬁ', 'r', '\u202c', 'l', '@', '9', 'ú', '×', '㩶', '°', 'ñ', 'ž', 'â', '{', '0', '\uf028', '¶', '′', '½', 'î', '\x88', 'ë', 'b', '♦', '>', 'i', ':', ')', '★', 'w', '㩠', '·', 'm', '\u2002', '‐', 'é', 't', '…', '|', '¼', '^', '⅛', '\x9a', '~', 'û', '•', '&', 'e', '¿', '●', '[', '–', '#', '(', '\uf02e', 'ƒ', '\u2009', 'ʼ', 'd', '\uf06e', 'ù', '1', '¢', 'º', "'", 'ô', '‑', 'ç', '≠', 'o', '4', '∆', 'ê', 'a', 'y', '‹', '¹', '☆', '❤', '\ufeff', '3', 'ŷ', '®', 'á', '\x80', '\x8a', '$', '—', '_', 'ã', 'ü', '©', '\u202a', '‚', '-', '¯', '¡', 'v', '"', 'è', '’', '\U000f4d25', '”', '¬', '�', '8', '»', '=', 'ö', '‘', '}', '\u200b', 'x', '̃', 'þ', '\x83', '\x85', 'ó', '“', '\ue00d', '₂', 'u', '₤', '̈', 'ò', '″', 'p', '†', '!', 'f', '́'] + [UNK_TOKEN, START_TOKEN]
CHAR_COUNT = len(chars)
MAXLEN = 40
LSTM_BATCH_SIZE = 512
EM = 10
LR = 0.001
char_indices = dict((c, i) for i, c in enumerate(chars))

def pad(tweet, start_token=START_TOKEN):
    """
    helper function to pad the training and testing data in order to get the probabilities for the start of the sentence!
    """
    if len(tweet) <= MAXLEN:
        return (start_token*(MAXLEN-len(tweet)+1)) + tweet
    else:
        return start_token+tweet
    #return (start_token*MAXLEN) + tweet

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
    helper function to get the log probability for each tweet
    """
    sp = 0
    for i in range(len(l)):
        # log probability
        if math.log10(l[i]) != 0:
            sp += math.log10(l[i])
    return sp/len(l)