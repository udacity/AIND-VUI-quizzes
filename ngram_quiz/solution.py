from collections import Counter

import numpy as np
from nltk.util import ngrams

import ngram_quiz.utils as utils

def main():
    # test the following sentences
    test_sentences = [
        'the old man spoke to me',
        'me to spoke man old the',
        'old man me old man me',
    ]

    tokens, bigrams = utils.bigrams_from_transcript('transcripts.txt')
    bigram_raw_counts = Counter(bigrams)
    tokens_raw_counts = Counter(tokens)

    bg_mle_dict_ll = bigram_mle_loglikelihood(bigram_raw_counts, tokens_raw_counts)
    bg_addone_dict_ll = add_one_smoothing_log_likelihood(bigram_raw_counts, tokens_raw_counts)

    most_likely = ''
    highest_likelihood = float('-inf')

    for sentence in test_sentences:
        print('Test sentence: {}:'.format(sentence))
        print('log of maximum likelihood estimate: {}'.format((sentence_loglikelihood(sentence, bg_mle_dict_ll))))
        print('log of Laplace Add-one smoothed estimate: {}'.format((sentence_loglikelihood(sentence, bg_addone_dict_ll))))

def sentence_loglikelihood(sentence, loglikelihood_dict):
    s_tokens = ['<s>'] + sentence.split() + ['</s>']
    ll = 0.
    for bg in ngrams(s_tokens, 2):
        if bg in loglikelihood_dict:
            ll = ll + loglikelihood_dict[bg]
        else:
            ll = ll + loglikelihood_dict['<unk>']
    return ll


def bigram_mle_loglikelihood(bigram_counts, token_counts):
    # Dan Jurafsky slide #15, #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    bg_mle_dict = {}
    for bg in bigram_counts:
        bg_mle_dict[bg] = np.log(bigram_counts[bg] / token_counts[bg[0]])
    bg_mle_dict['<unk>'] = float('-inf')
    return bg_mle_dict


def add_one_smoothing_log_likelihood(bigram_counts, token_counts):
    vocab_count = len(token_counts)
    bg_addone_dict = {}
    for bg in bigram_counts:
        bg_addone_dict[bg] = np.log((bigram_counts[bg] + 1) / (token_counts[bg[0]] + vocab_count))
    bg_addone_dict['<unk>'] = np.log(1 / vocab_count)
    # https: // en.wikipedia.org / wiki / Additive_smoothing
    # Dan Jurafsky slide #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    return bg_addone_dict


if __name__ == '__main__':
    main()



    # bg_mle_dict = bigram_mle(bigram_raw_counts, tokens_raw_counts)
    # bg_addone_dict = add_one_smoothing(bigram_raw_counts, tokens_raw_counts)
    # print(sentence_prob('the old man spoke to me', bg_mle_dict))
    # print(sentence_prob('the old man spoke to me', bg_addone_dict))
    # def sentence_prob(sentence, prob_dict):
    #     s_tokens = ['<s>'] + sentence.split() + ['</s>']
    #     prob = 1
    #     for bg in ngrams(s_tokens, 2):
    #         if bg in prob_dict:
    #             prob = prob * prob_dict[bg]
    #         else:
    #             prob = prob * prob_dict['<unk>']
    #     return prob



    # def add_one_smoothing(bigram_counts, token_counts):
    #     vocab_count = len(token_counts)
    #     bg_addone_dict = {}
    #     for bg in bigram_counts:
    #         bg_addone_dict[bg] = (bigram_counts[bg] + 1) / (token_counts[bg[0]] + vocab_count)
    #     bg_addone_dict['<unk>'] = 1 / vocab_count
    #     # https: // en.wikipedia.org / wiki / Additive_smoothing
    #     # Dan Jurafsky slide #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    #     return bg_addone_dict


    # def bigram_mle(bigram_counts, token_counts):
    #     # Dan Jurafsky slide #15, #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    #     bg_mle_dict = {}
    #     for bg in bigram_counts:
    #         bg_mle_dict[bg] = bigram_counts[bg] / token_counts[bg[0]]
    #     bg_mle_dict['<unk>'] = 0
    #     return bg_mle_dict
