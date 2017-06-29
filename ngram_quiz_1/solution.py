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
    sentence_tokens = ['<s>'] + nltk.word_tokenize(sentence.lower()) + ['</s>']
    sentence_bigrams = list(ngrams(sentence_tokens, 2))
    return sentence_tokens, sentence_bigrams


if __name__ == '__main__':
    for sentence in test_sentences:
        print('\n*** Sentence: "{}"'.format(sentence))
        t, b = sentence_to_bigrams(sentence)
        print('tokens = {}'.format(t))
        print('bigrams = {}'.format(b))
