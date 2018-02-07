'''
Feb 2018
Deep Learning method for Humor Detection
Xinru Yan

This program pre processes the training data. It takes a file as input,
reads 2**20 lines at a time (line_batchsize), pre process it and puts the pre_processed data into an npz file (e.g. data_0.npz).
In the end it outputs a folder including all the npz files and a file including how many sequences it pre_processed in total

line_batchsize can be changed in the main() function

Pre process prepares the data into X and Y (inputs and outputs) pairs:
X: training data input (a fixed length of chars)
Y: training data predict output (the next char)

Usage:
    python3 pre_process.py INPUT_FILE OUTPUT_FOLDER
    e.g.:
    python3 ../../NgramLM/mydata/plain.txt ../mydata/npz_files/tweets

'''
import numpy as np
import sys
import os
import preprocessor as p
import shutil
import time

from config import *


class SentencePreProcessor(object):
    def __init__(self, in_filename, out_dir, sentences_per_file, debug=False):
        self.in_filename = in_filename
        self.sentences_per_file = sentences_per_file
        self.out_dir = out_dir
        self.cur_output_file = 0
        self.sentences = []
        self.next_chars = []
        # debug signal, set to true
        self.debug = debug
        self.p_bar_start = 0
        self.bytes_cleaned = 0
        self.total_sentence_count = 0
        self.p_bar_length = 70

    def get_p_bar(self, i, t):
        """
        helper function to see the progress made and an ETA
        :return: progress bar
        """

        if self.p_bar_start == 0 or i == 0:
            self.p_bar_start = time.time()
            return ""
        if i/t == 1:
            return "\r[{}] {}/{} Took: {:.2f} sec".format("*"*self.p_bar_length, t, t, time.time()-self.p_bar_start)
        stars = round((i / t) * self.p_bar_length)
        spaces = self.p_bar_length - stars
        past_time = time.time()-self.p_bar_start
        time_per_i = past_time/i
        estimated_total_time = time_per_i*t
        eta = estimated_total_time - past_time
        return "\r[{}{}] {}/{} ETA: {:.2f} sec".format("*"*stars, " "*spaces, i, t, eta)

    def clean_line(self, line):
        """
        clean each line of input file (string to int convert, padding, lowercase, tweet clean)
        :param line: line in the input file
        :return: cleaned version of line
        """
        if self.debug:
            self.bytes_cleaned += len(line)
        return text2ints(pad(p.clean(line.lower()).replace("\n", " ")))

    def __dump(self, amount):
        """
        save the X = sentences[] and Y = next_chars[] to an npz file
        :param amount: line_batchsize
        """
        X = np.asarray(self.sentences[:amount], dtype="int8")
        Y = np.asarray(self.next_chars[:amount], dtype="int8")
        self.total_sentence_count += len(X)
        np.savez("{}/data_{}.npz".format(self.out_dir, self.cur_output_file), x=X, y=Y)
        self.sentences = self.sentences[amount:]
        self.next_chars = self.next_chars[amount:]
        self.cur_output_file += 1

    def dump_sentences(self):
        """
        dump each batch of sentences once reach the line_batchsize
        """
        while len(self.sentences) >= self.sentences_per_file:
            self.__dump(self.sentences_per_file)

    def run(self):
        # remove output directory if exists and remake it.
        if os.path.exists(self.out_dir):
            shutil.rmtree(self.out_dir)
        os.mkdir(self.out_dir)

        # Setup
        self.total_sentence_count = 0
        self.cur_output_file = 0
        self.sentences = []
        self.next_chars = []

        file_length = None
        i = 0
        if self.debug:
            self.bytes_cleaned = 0
            file_length = os.path.getsize(self.in_filename)

        if self.debug:
            sys.stdout.write(self.get_p_bar(0, 1))
        with open(self.in_filename, "r", encoding='UTF-8') as f:
            for line in map(self.clean_line, f):
                if self.debug:
                    if i % 400 == 0:
                        sys.stdout.write(self.get_p_bar(self.bytes_cleaned, file_length))
                        sys.stdout.flush()
                    i += 1
                # fixed length of sequence: MAXLEN, jump STEP each time
                for j in range(0, len(line) - MAXLEN, STEP):
                    self.sentences.append(line[j: j + MAXLEN])
                    self.next_chars.append(line[j + MAXLEN])
                self.dump_sentences()
            self.__dump(len(self.sentences))
        with open("{}/data_count".format(self.out_dir), "w") as f:
            f.write(str(self.total_sentence_count))
        if self.debug:
            sys.stdout.write(self.get_p_bar(file_length, file_length))


def main():
    # the training corpus
    in_filename = sys.argv[1]
    # the output directory name
    out_dir = sys.argv[2]
    # 2**20 is the line_batchsize (process 2**20 lines at a time and save to an npz file)
    SentencePreProcessor(in_filename, out_dir, 2**20, debug=True).run()

if __name__ == '__main__':
    main()
