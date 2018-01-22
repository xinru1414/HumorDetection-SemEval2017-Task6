from __future__ import print_function


from nltk.tokenize import TweetTokenizer
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM


class LSTMModel(Model):
    max_features = 200000
    max_len = 70
    batch_size = 32

    def __init__(self):
        self.tokenize = TweetTokenizer(preserve_case=False).tokenize

    def train(self, tweets):
        """
        Set up the model
        Args:
            tweets(List[Tweet]): a list of tweets/sentences
        """
        self.vocab = {}  # the vocab of the corpus; a dictionary
        self.reverse_vocab = {} # for debug
        x, y = [], [] # training input and output. Input is the tweet. Output is the class (0, 1 or 2. For News data, all news belong to 0)
        for tweet in tweets:
            x += [self.__vectorize(tweet.tweet)]
            y += [tweet.label]

        print("Example vectors: {}".format(x[:5])) #for debug
        print("First: {}".format(self.__unvectorize(x[0]))) #for debug

        x = sequence.pad_sequences(x, maxlen=self.max_len) #pad it so they have the same length as defined above

        self.model = Sequential()
        self.model.add(Embedding(self.max_features, 128)) # first step: word_embedding
        self.model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2)) #apply LSTM
        self.model.add(Dense(1, activation='sigmoid')) #parameter setting

        # try using different optimizers and different optimizer configs
        self.model.compile(loss='binary_crossentropy',
                           optimizer='adam',
                           metrics=['accuracy'])

        self.model.fit(x, y, batch_size=self.batch_size, epochs=1)

    def __vectorize(self, text):
        """
        Vectorize the tweet/sentence
        Args:
            text(text): The text to vectorize.
        """
        vectorized_text = []  # list of vectorized text
        for token in self.tokenize(text):
            if token not in self.vocab:
                self.vocab[token] = len(self.vocab)  # if the token is not in the vocab, token => key, int number => value
                self.reverse_vocab[self.vocab[token]] = token
            vectorized_text += [self.vocab[token]]
        return tuple(vectorized_text)

    def __unvectorize(self, vector):
        """
        For debugging purpose
        """
        return " ".join(map(lambda x: self.reverse_vocab[x], vector))

    def predict(self, text):
        """
        for testing data
        :param text: testing tweet
        :return: a probability
        """
        text = self.__vectorize(text)
        text = sequence.pad_sequences([text], maxlen=self.max_len)
        return self.model.predict(text, verbose=0)[0][0]



