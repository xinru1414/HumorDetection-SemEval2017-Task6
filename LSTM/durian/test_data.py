from keras.models import load_model
import numpy as np
from config import *

def get_sentence_prob(sentence):
    """
    helper function to get the probabilities and keep things moving to the next
    """
    seed = sentence[:MAXLEN]
    assert len(seed) == MAXLEN
    sent_preds = []

    for i in range(len(sentence)-MAXLEN):
        x = np.zeros((1, MAXLEN), dtype=np.int8)
        for char_index, char in enumerate(seed):
            x[0, char_index] = char

        preds = model.predict(x, verbose=0)[0]
        sent_preds += [preds[sentence[MAXLEN + i]]]
        # keep it moving to the next
        seed = sentence[i:MAXLEN + i]
    return sent_preds

for iteration in range(1, 2):
    print()
    print('-' * 50)
    print('Iteration', iteration)
    model = load_model('model_tweets.h5')
    # you get to see the probabilities. notice that padding of the testing data happens here
    print(pad("i am jim"))
    print(text2ints(pad("i am jim")))
    print(get_sentence_prob(text2ints(pad("i am jim"))))

print("\nThe final probability for sentences: ")
print("i am jim", get_prob(get_sentence_prob(text2ints(pad("i am jim")))))