from keras.models import load_model
import sys
from config import *
from score import get_sentence_prob

MODELNAME = sys.argv[1]
FILENAME = sys.argv[2]

def read(filename):
    with open(filename, "r", encoding='UTF-8') as f:
        text = f.read().splitlines()
    return text

def main():
    model = load_model(MODELNAME)
    text = read(FILENAME)
    for t in text:
        print(t)
        t = text2ints(pad(t))
        print(get_prob(get_sentence_prob(model, t)), get_sentence_prob(model, t), "\n")

if __name__ == '__main__':
    main()