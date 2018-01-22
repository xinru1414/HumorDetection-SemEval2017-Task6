import numpy as np
import sys
from config import *

# the training corpus
FILENAME =  sys.argv[1]
# the output file name
NPFILE =  sys.argv[2]


def read_file(filename):
    """
    read in input file as lower_case text, get rid of new line and return text as string
    """
    text = []
    with open(filename, "r", encoding='UTF-8') as f:
        for line in f:
            text += text2ints(pad(line.lower().replace("\n", " ")))
    return text


def main():
    print("Reading tweet file...")
    # read in the file
    text = read_file(FILENAME)
    print('corpus length:', len(text), flush=True)
    # print(text)
    print('total chars:', len(chars))

    # preprocess the text in semi-redundant sequences of maxlen characters
    sentences = []
    next_chars = []
    for i in range(0, len(text) - MAXLEN, STEP):
        sentences.append(text[i: i + MAXLEN])
        next_chars.append(text[i + MAXLEN])

    print('nb sequences:', len(sentences))
    # print("normal sentences:")
    # print(sentences)
    sentences = np.asarray(sentences, dtype='int8')
    next_chars = np.asarray(next_chars, dtype='int8')
    # print("np sentences:")
    # print(sentences)
    # print(next_chars)

    print("saving...")
    np.savez(NPFILE, x=sentences, y=next_chars)
    # npzfile = np.load(NPFILE)
    #
    # sentences = npzfile['x']
    # next_chars = npzfile['y']
    #
    # print("after loading")
    # print(sentences)
    # print(next_chars)

if __name__ == '__main__':
    main()
