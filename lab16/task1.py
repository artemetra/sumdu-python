import nltk
import matplotlib.pyplot as plt
from collections import Counter

try:
    with open("melville-moby_dick.txt", "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)


def count_words(text):
    sentences = nltk.sent_tokenize(text)
    k_words = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        # words - список зі словами
        k_words += len(words)
    return k_words


def most_used_words(text):
    text1 = text.split()
    cnt = Counter(text1)
    cort = cnt.most_common(10)
    x = [el[0] for el in cort]
    y = [el[1] for el in cort]
    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()


print("Кількість слів:", count_words(text))
most_used_words(text)
