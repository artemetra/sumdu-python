import string
import re

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

RESULT = "result.txt"


def tokenize(text):
    return word_tokenize(text)


def stem(text):
    ps = PorterStemmer()
    return [ps.stem(w) for w in tokenize(text)]


def lemmatize(text):
    wnl = WordNetLemmatizer()
    return [wnl.lemmatize(w) for w in tokenize(text)]


def del_punctuation(text):
    l = nltk.word_tokenize(text)
    ll = [x for x in l if not re.fullmatch("[" + string.punctuation + "]+", x)]
    return ll


input_text = (
    "- Hey, where did you get that beautiful shirt?"
    " - Oh, from the glamorous shirt store!"
    "It's on the outskirts, you should give it a visit someday."
)
with open(RESULT, "w") as f:
    f.write("Original:\n")
    f.write(input_text)
    f.write("\n\n")

    f.write("Tokenized:\n")
    f.write(" | ".join(tokenize(input_text)))
    f.write("\n\n")

    f.write("Stemmed:\n")
    f.write(" | ".join(stem(input_text)))
    f.write("\n\n")

    f.write("Lemmas:\n")
    f.write(" | ".join(lemmatize(input_text)))
    f.write("\n\n")

    f.write("Without punctuation:\n")
    f.write(" | ".join(del_punctuation(input_text)))
