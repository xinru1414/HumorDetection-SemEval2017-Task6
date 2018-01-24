class Tweet(object):
    def __init__(self, tweet, label):
        """
        Args:
            :param tweet: the text of the tweet/sentence
            :param label: the label of the tweet/sentence
        """
        self.tweet = tweet
        self.label = label

class Model(object):
    def train(self, tweets):
        """
        Args:
            :param tweets: a list of tweets/sentences
        """
        raise NotImplementedError("This is an abstract method")

    def predict(self, tweet):
        """
        Args:
            :param tweet: the tweet that needs to be scored
        Return:
            float: the probability of the tweet
        """
        raise NotImplementedError("This is an abstract method")


