## Probabilities and Likelihoods with Bigrams

Recall from a previous video that the probability of a series of words
can be calculated from the chained probabilities of its history:

`the equation`

Our concrete example:

`the example P("I love language models ...) use mathquill here`

The probabilities of sequence occurrences in a large textual corpus can be calculated this
way and used as a language model to add grammar and contectual knowledge to a speech
recognition system.  However, there are a few problems with this approach in practice:
1. There is a prohibitively large number of calculations for all the 
possible sequences of varying length in a large textual corpus.  
2. Even if we're able to calculate, store, and search all combinations from a textual corpus to "train"
the probabilities, some possible combinations will not exist that might be queried later
because language is creative.
3. Repeated multiplications of small probabilitie can cause underflow problems in computers when
the values become to small.

To address the first problem, we use the [Markov Assumption]() which allows us to approximate
a sequence probability with a shorter sequence.  We should expect longer sequences to provide better
approximations, but in the bigram case, the equation reduces to:

`the reduced equation`

Concrete example:

`example`



## Quiz 2 Instructions

In the quiz below, write a function that returns a list of tokens and a list of bigrams for a given sentence.  You will need to first break a sentence into words in a list, then add a `<s>` and `<s/>` token to the
start and end of the list to represent the start and end of the sentence.

Your final lists should be in the format shown above and called out in the function docstring.