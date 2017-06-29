from collections import Counter

import nltk
import numpy as np
from nltk.util import ngrams


def total_counts(counter):
    result = sum(counter[key] for key in counter)
    return result


def sentence_prob(sentence, prob_dict):
    s_tokens = ['<s>'] + sentence.split() + ['</s>']
    prob = 1
    for bg in ngrams(s_tokens, 2):
        if bg in prob_dict:
            prob = prob * prob_dict[bg]
        else:
            prob = prob * prob_dict['<unk>']
    return prob


def sentence_loglikelihood(sentence, loglikelihood_dict):
    s_tokens = ['<s>'] + sentence.split() + ['</s>']
    ll = 0.
    for bg in ngrams(s_tokens, 2):
        if bg in loglikelihood_dict:
            ll = ll + loglikelihood_dict[bg]
        else:
            ll = ll + loglikelihood_dict['<unk>']
    return ll


def bigram_mle(bigram_counts, token_counts):
    # Dan Jurafsky slide #15, #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    bg_mle_dict = {}
    for bg in bigram_counts:
        bg_mle_dict[bg] = bigram_counts[bg] / token_counts[bg[0]]
    bg_mle_dict['<unk>'] = 0
    return bg_mle_dict


def bigram_mle_loglikelihood(bigram_counts, token_counts):
    # Dan Jurafsky slide #15, #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    bg_mle_dict = {}
    for bg in bigram_counts:
        bg_mle_dict[bg] = np.log(bigram_counts[bg] / token_counts[bg[0]])
    bg_mle_dict['<unk>'] = float('-inf')
    return bg_mle_dict


def add_one_smoothing(bigram_counts, token_counts):
    vocab_count = len(token_counts)
    bg_addone_dict = {}
    for bg in bigram_counts:
        bg_addone_dict[bg] = (bigram_counts[bg] + 1) / (token_counts[bg[0]] + vocab_count)
    bg_addone_dict['<unk>'] = 1 / vocab_count
    # https: // en.wikipedia.org / wiki / Additive_smoothing
    # Dan Jurafsky slide #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    return bg_addone_dict


def add_one_smoothing_log_likelihood(bigram_counts, token_counts):
    vocab_count = len(token_counts)
    bg_addone_dict = {}
    for bg in bigram_counts:
        bg_addone_dict[bg] = np.log((bigram_counts[bg] + 1) / (token_counts[bg[0]] + vocab_count))
    bg_addone_dict['<unk>'] = np.log(1 / vocab_count)
    # https: // en.wikipedia.org / wiki / Additive_smoothing
    # Dan Jurafsky slide #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    return bg_addone_dict


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


if __name__ == '__main__':
    tokens, bigrams = bigrams_from_sentences('transcripts.txt')
    bigram_raw_counts = Counter(bigrams)
    tokens_raw_counts = Counter(tokens)

    bg_mle_dict = bigram_mle(bigram_raw_counts, tokens_raw_counts)
    bg_addone_dict = add_one_smoothing(bigram_raw_counts, tokens_raw_counts)
    print(sentence_prob('the old man spoke to me', bg_mle_dict))
    print(sentence_prob('the old man spoke to me', bg_addone_dict))

    bg_mle_dict_ll = bigram_mle_loglikelihood(bigram_raw_counts, tokens_raw_counts)
    bg_addone_dict_ll = add_one_smoothing_log_likelihood(bigram_raw_counts, tokens_raw_counts)
    print(sentence_loglikelihood('the old man spoke to me', bg_mle_dict_ll))
    print(sentence_loglikelihood('the old man spoke to me', bg_addone_dict_ll))
