import sys, os
# the kenlm languge model
import kenlm

MODELNAME = sys.argv[1]
FILENAME = sys.argv[2]
RESULT = sys.argv[3]

def read(filename):
    with open(filename, "r") as f:
        text = f.read().splitlines()
    return text

def main():
    model = kenlm.Model(MODELNAME)
    text = read(FILENAME)
    with open(RESULT, 'w') as o:
        for t in text:
            o.writelines(t + " " + str(model.score(t, bos = False, eos = False))+"\n")
if __name__ == '__main__':
    main()