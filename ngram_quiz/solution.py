import nltk
from nltk.util import ngrams
from collections import Counter
import ngram_quiz.utils as utils
import urllib.request

# https://stackoverflow.com/questions/32441605/generating-ngrams-unigrams-bigrams-etc-from-a-large-corpus-of-txt-files-and-t

def make_ngrams1():
    # text = "I need to write a program in NLTK that breaks a corpus (a large collection of \
    # txt files) into unigrams, bigrams, trigrams, fourgrams and fivegrams.\
    # I need to write a program in NLTK that breaks a corpus"
    text = "GO DO YOU HEAR BUT IN LESS THAN FIVE MINUTES THE STAIRCASE GROANED BENEATH \
    AN EXTRAORDINARY WEIGHT AT THIS MOMENT THE WHOLE SOUL OF THE OLD MAN SEEMED CENTRED \
    IN HIS EYES WHICH BECAME BLOODSHOT THE VEINS OF THE THROAT SWELLED HIS CHEEKS AND \
    TEMPLES BECAME PURPLE AS THOUGH HE WAS STRUCK WITH EPILEPSY NOTHING WAS WANTING TO \
    COMPLETE THIS BUT THE UTTERANCE OF A CRY AND THE CRY ISSUED FROM HIS PORES IF WE MAY \
    THUS SPEAK A CRY FRIGHTFUL IN ITS SILENCE DAVRIGNY RUSHED TOWARDS THE OLD MAN AND \
    MADE HIM INHALE A POWERFUL RESTORATIVE DAVRIGNY UNABLE TO BEAR THE SIGHT OF THIS \
    TOUCHING EMOTION TURNED AWAY AND VILLEFORT WITHOUT SEEKING ANY FURTHER EXPLANATION \
    AND ATTRACTED TOWARDS HIM BY THE IRRESISTIBLE MAGNETISM WHICH DRAWS US TOWARDS \
    THOSE WHO HAVE LOVED THE PEOPLE FOR WHOM WE MOURN EXTENDED HIS HAND TOWARDS THE \
    YOUNG MAN FOR SOME TIME NOTHING WAS HEARD IN THAT CHAMBER BUT SOBS EXCLAMATIONS \
    AND PRAYERS WHAT DO YOU MEAN SIR OH YOU RAVE SIR EXCLAIMED VILLEFORT IN VAIN \
    ENDEAVORING TO ESCAPE THE NET IN WHICH HE WAS TAKEN I RAVE DO YOU KNOW THE ASSASSIN \
    ASKED MORREL NOIRTIER LOOKED UPON MORREL WITH ONE OF THOSE MELANCHOLY SMILES WHICH \
    HAD SO OFTEN MADE VALENTINE HAPPY AND THUS FIXED HIS ATTENTION SAID MORREL SADLY \
    YES REPLIED NOIRTIER THE OLD MANS EYES REMAINED FIXED ON THE DOOR ASKED MORREL YES \
    MUST I LEAVE ALONE NO BUT CAN HE UNDERSTAND YOU YES GENTLEMEN HE SAID IN A HOARSE \
    VOICE GIVE ME YOUR WORD OF HONOR THAT THIS HORRIBLE SECRET SHALL FOREVER REMAIN \
    BURIED AMONGST OURSELVES THE TWO MEN DREW BACK MY FATHER HAS REVEALED THE CULPRITS \
    NAME MY FATHER THIRSTS FOR REVENGE AS MUCH AS YOU DO YET EVEN HE CONJURES YOU AS \
    I DO TO KEEP THIS SECRET DO YOU NOT FATHER MORREL SUFFERED AN EXCLAMATION OF \
    HORROR AND SURPRISE TO ESCAPE HIM THE OLD MAN MADE A SIGN IN THE AFFIRMATIVE IT \
    WAS SOMETHING TERRIBLE TO WITNESS THE SILENT AGONY THE MUTE DESPAIR OF NOIRTIER \
    WHOSE TEARS SILENTLY ROLLED DOWN HIS CHEEKS BUT HE STOPPED ON THE LANDING HE HAD \
    NOT THE COURAGE TO AGAIN VISIT THE DEATH CHAMBER THE TWO DOCTORS THEREFORE ENTERED \
    THE ROOM ALONE NOIRTIER WAS NEAR THE BED PALE MOTIONLESS AND SILENT AS THE CORPSE \
    THE DISTRICT DOCTOR APPROACHED WITH THE INDIFFERENCE OF A MAN ACCUSTOMED TO SPEND \
    HALF HIS TIME AMONGST THE DEAD HE THEN LIFTED THE SHEET WHICH WAS PLACED OVER THE \
    FACE AND JUST UNCLOSED THE LIPS THE NEAREST SAID THE DISTRICT DOCTOR IS A GOOD \
    ITALIAN ABBE WHO LIVES NEXT DOOR TO YOU SHALL I CALL ON HIM AS I PASS DAVRIGNY \
    SAID VILLEFORT BE SO KIND I BESEECH YOU AS TO ACCOMPANY THIS GENTLEMAN HERE IS \
    THE KEY OF THE DOOR SO THAT YOU CAN GO IN AND OUT AS YOU PLEASE YOU WILL BRING \
    THE PRIEST WITH YOU AND WILL OBLIGE ME BY INTRODUCING HIM INTO MY CHILDS ROOM \
    DO YOU WISH TO SEE HIM I ONLY WISH TO BE ALONE YOU WILL EXCUSE ME WILL YOU NOT \
    I AM GOING SIR AND I DO NOT HESITATE TO SAY THAT NO PRAYERS WILL BE MORE FERVENT THAN MINE"
    # TargetURL = 'https://sherlock-holm.es/stories/plain-text/cnus.txt'
    # webfile = urllib.request.urlopen(TargetURL)
    # text = webfile.read(20000)
    # alltext = ''
    # for line in text:
    #     alltext = alltext + str(line)
    # text = 'just three words'
    tokens = nltk.word_tokenize(text.lower())
    print(tokens)
    unigrams = ngrams(tokens, 1)
    bigrams = ngrams(tokens, 2)
    # trigrams = ngrams(tokens, 3)
    # # fourgrams = ngrams(tokens, 4)
    # # fivegrams = ngrams(tokens, 5)

    uni_counted = Counter(unigrams)
    bi_counted = Counter(bigrams)
    # tri_counted = Counter(trigrams)
    # print(uni_counted)
    print(uni_counted.most_common(10))
    print(bi_counted.most_common(10))
    # print(tri_counted.most_common(10))

    print(total_counts(uni_counted))
    print("probability of word 'the': {}".format(prob_uni_ngram('the',uni_counted)))
    print("probability of word 'gobbledegook': {}".format(prob_uni_ngram('gobbledegook',uni_counted)))
    print("probability of word 'the old': {}".format(prob_bi_ngram('the', 'old',bi_counted)))
    print("probability of word 'the gobbledegook': {}".format(prob_bi_ngram('the','gobbledegook',bi_counted)))
    # fdist = nltk.FreqDist(bigrams)
    # for k, v in fdist.items():
    #     print(" k: {} v: {}".format(k, v))

# def ll_3gram(three_word_string):
#     three_list = three_word_string.split()
#     prob_all = prob_ngram(three_list[0],1)
#     pass

def prob_uni_ngram(word, counter):
    print(counter[(word,)])
    if not counter[(word,)]:
        print("did not find {}".format(word))
        return 1/(total_counts(counter)+1)
    else:
        return counter[(word,)]/total_counts(counter)

def prob_bi_ngram(word1, word2, counter):
    print(counter[(word1, word2)])
    if not counter[(word1, word2)]:
        print("did not find {},{}".format(word1, word2))
        return 1/(total_counts(counter)+1)
    else:
        return counter[(word1, word2)]/total_counts(counter)
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
            print('{} not in dict'.format(bg))
    return prob


def bigram_mle(bigram_counts, token_counts):
    # Dan Jurafsky slide #15, #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    bg_mle_dict = {}
    for bg in bigram_counts:
        bg_mle_dict[bg] = bigram_counts[bg] / token_counts[bg[0]]
    return bg_mle_dict


def add_one_smoothing(bigram_counts, token_counts):
    vocab_count = len(token_counts)
    bg_addone_dict = {}
    for bg in bigram_counts:
        bg_addone_dict[bg] = (bigram_counts[bg] + 1) / (token_counts[bg[0]] + vocab_count)
    bg_addone_dict['<unk>'] = 1/vocab_count
    # https: // en.wikipedia.org / wiki / Additive_smoothing
    # Dan Jurafsky slide #47 :https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf
    return bg_addone_dict

if __name__ == '__main__':

    tokens, bigrams = utils.bigrams_from_sentences('transcripts.txt')
    bigram_raw_counts = Counter(bigrams)
    print(bigram_raw_counts)
    tokens_raw_counts = Counter(tokens)
    bg_mle_dict = bigram_mle(bigram_raw_counts, tokens_raw_counts)
    print(bg_mle_dict)
    print(sentence_prob('the old man spoke to me', bg_mle_dict))
    print("vocab count single = {}".format(len(tokens_raw_counts)))
    print("vocab coun bigrams = {}".format(len(bigram_raw_counts)))



