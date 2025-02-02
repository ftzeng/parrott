'''
Parrott
======================
By Francis Tseng (@frnsys)

A pseudo-intelligent auto-retweeter.
'''

import sys
import naive_bayes
import membrane
from memory import Memory

class Parrott:
    def __init__(self):
        '''
        Births a new Parrott,
        with a Naive Bayes brain
        and a Solr memory.
        '''
        self.brain = naive_bayes.NaiveBayes()
        self.twitter = membrane.twitter.api()
        self.memory = Memory()

    def train(self):
        '''
        Trains the Parrott on examples
        stored in Memory (Solr)
        '''
        # Fetch 1000 positive and negative examples.
        pos_tweets = self.memory.recall_positive(0, 1000)
        neg_tweets = self.memory.recall_negative(0, 1000)

        # Pull out the proper text for training data.
        pos = [' '.join([tweet['tweet'], tweet['user']]) for tweet in pos_tweets]
        neg = [' '.join([tweet['tweet'], tweet['user']]) for tweet in neg_tweets]

        # Train the brain.
        self.brain.train(pos, neg)

    def test(self, pos_set, neg_set, threshold=0.8):
        '''
        Tests the Parrott on a set of positive
        and negative examples.

        Args:
            pos_set (list): positive test examples
            neg_set (list): negative test examples
            threshold (float): testing threshold
        Returns:
            dict of test results.
        '''
        return self.brain.test(threshold, pos_set, neg_set)

    def classify(self, tweet):
        '''
        Classifies a Tweet.

        Args:
            tweet (string): the Tweet content
        Returns:
            probability of positive classification.
        '''
        return self.brain.classify(tweet)

    def audit(self, tweet, pos):
        '''
        Deletes an existing Tweet from Memory
        and replaces it with the updated Tweet.

        Args:
            tweet (dict): the Tweet to audit
            pos (bool): is the Tweet is a positive example?
        '''

        # Solr cannot "update", just delete & add.
        self.memory.forget(tweet)

        # Update the tweet.
        tweet.update({'positive':pos, 'audited':True})

        # Clear id and _version_ to prevent conflicts.
        del tweet['id']
        del tweet['_version_']

        # Re-memorize.
        self.memory.memorize(tweet)

