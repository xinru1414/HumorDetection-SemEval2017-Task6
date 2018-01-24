import re
from keras.models import load_model
import preprocessor as p
import sys

import numpy as np
from config import *

FILENAME = sys.argv[1]

model = load_model(FILENAME)

def get_sentence_prob(sentence):
    """
    helper function to get the probabilities and keep things moving to the next
    """
    seed = sentence[:MAXLEN]
    assert len(seed) == MAXLEN
    sent_preds = []

    for i in range(len(sentence) - MAXLEN):
        x = np.zeros((1, MAXLEN), dtype=np.int8)
        for char_index, char in enumerate(seed):
            x[0, char_index] = char

        preds = model.predict(x, verbose=0)[0]
        sent_preds += [preds[sentence[MAXLEN + i]]]
        # keep it moving to the next
        seed = sentence[i:MAXLEN + i]
    return sent_preds

rt1 = 'i need to vent.'
rt2 = 'his timing was good.'
rt3 = 'need i to vent. '
rt4 = 'timing his good was.'
rt5 = 'I need to Vent.'
rt6 = 'alksd lasgd fh'

print(rt1)
rt1 = text2ints(pad(rt1))
print(get_prob(get_sentence_prob(rt1)), get_sentence_prob(rt1))

print(rt2)
rt2 = text2ints(pad(rt2))
print(get_prob(get_sentence_prob(rt2)), get_sentence_prob(rt2))

print(rt3)
rt3 = text2ints(pad(rt3))
print(get_prob(get_sentence_prob(rt3)), get_sentence_prob(rt3))

print(rt4)
rt4 = text2ints(pad(rt4))
print(get_prob(get_sentence_prob(rt4)), get_sentence_prob(rt4))

print(rt5)
rt5 = text2ints(pad(rt5))
print(get_prob(get_sentence_prob(rt5)), get_sentence_prob(rt5))

print(rt6)
rt6 = text2ints(pad(rt6))
print(get_prob(get_sentence_prob(rt6)), get_sentence_prob(rt6))
