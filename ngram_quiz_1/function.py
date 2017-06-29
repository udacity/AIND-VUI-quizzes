from collections import Counter

import nltk
from nltk import ngrams

test_sentences = [
    'the old man spoke to me',
    'me to spoke man old the',
    'old man me old man me',
]

def sentence_to_bigrams(sentence):
    """
    Add start '<s>' and stop <'/s> tags to the sentence and tokenize it into a list
    of words (sentence_tokens) and bigrams (sentence_bigrams)
    :param sentence: string
    :return: list, list
        sentence_tokens: ordered list of words found in the sentence
        sentence_bigrams: a list of ordered two-word tuples found in the sentence
    """
    #TODO implement
    sentence_tokens = None
    sentence_bigrams = None
    return sentence_tokens, sentence_bigrams

