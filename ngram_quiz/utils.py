import os
import nltk
from nltk.util import ngrams
from collections import Counter

def bigrams_from_sentences(filename):
    # vocab = set()
    tokens = []
    bigrams = []
    with open(filename, 'r') as f:
        for line in f:
            line_tokens = ['<s>'] + nltk.word_tokenize(line.lower()) + ['</s>']
            bigrams = bigrams + list(ngrams(line_tokens, 2))
            # vocab = vocab.union(set(line_tokens))
            tokens = tokens + line_tokens
    return tokens, bigrams

