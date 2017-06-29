## Generating N-Grams

An N-Gram is an ordered sequence of words. For example:
![ngram example](../images/ngrams_numbers.png)
In the following series of quizes, you will work with 2-grams, or [bigrams](https://en.wikipedia.org/wiki/Bigram), as they are more commonly called.
The objective is to create a function that calculates the probability that a particular sentence
could occur in a corpus of text, based on the probabilities of its component bigrams.  We'll do this in stages though:
* Quiz 1 - Extract tokens and bigrams from a sentence
* Quiz 2 - Calculate probabilities and log likelihoods for bigrams
* Quiz 3 - Calculate the log likelihood of a given sentence based on a corpus of text using bigrams

#### Assumptions and terminology
We will assume that text data is in the form of sentences with no punctuation.  If a sentence is in a single line, we will add add a token for
start of sentence: `<s>` and end of sentence: `</s>`.  For example, if the sentence is "I love language models." it will appear in code as:

```
'I love language models'
```

The **tokens** for this sentence are represented as an ordered list of the lower case words plus the start and end sentence tags:

```
tokens = ['<s>', 'i', 'love', 'language', 'models', '</s>']
```

The **bigrams** for this sentence are represented as a list of lower case ordered pairs of tokens:

```
bigrams = [('<s>', 'i'), ('i', 'love'), ('love', 'language'), ('language', 'models'), ('models', '</s>')]
```

## Quiz 1 Instructions
The Natural Language Toolkit library, [nltk](http://www.nltk.org/) includes convenient tools for tokenizing and iterating ngrams over text. 
Here are the methods you will need:

* [nltk.word_tokenize()](http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.punkt.PunktLanguageVars.word_tokenize)
``` text
# usage:
In[1]: from nltk import word_tokenize
In[2]: token_list = word_tokenize('i love language models')
In[3]: token_list
Out[4]: ['i', 'love', 'language', 'models']
)
```

* [nltk.util.ngrams](http://www.nltk.org/api/nltk.html#module-nltk.util)
``` text
# ngrams is an iterator
# usage:
In[5]: from nltk.util import ngrams
In[6]: list(ngrams(token_list, 2))
Out[7]: [('I', 'love'), ('love', 'language'), ('language', 'models')]
```

In the quiz below, write a function that returns a list of tokens and a list of bigrams for a given sentence.  You will need to first break a sentence into words in a list, then add a `<s>` and `<s/>` token to the
start and end of the list to represent the start and end of the sentence.