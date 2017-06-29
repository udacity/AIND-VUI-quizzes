import nltk
from nltk import ngrams


def bigrams_from_transcript(filename):
    tokens = []
    bigrams = []
    with open(filename, 'r') as f:
        for line in f:
            line_tokens, line_bigrams = bigrams_from_sentence(line)
            tokens = tokens + line_tokens
            bigrams = bigrams + line_bigrams
    return tokens, bigrams


def bigrams_from_sentence(sentence):
    sentence_tokens = ['<s>'] + nltk.word_tokenize(sentence.lower()) + ['</s>']
    sentence_bigrams = list(ngrams(sentence_tokens, 2))
    return sentence_tokens, sentence_bigrams