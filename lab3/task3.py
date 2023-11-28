from collections import Counter

sentence = input("Введіть речення: ")
word_count = Counter(sentence.split(" "))
single_words = [w for (w, c) in word_count.items() if c==1]

print("Слова, що повторяються лише один раз:", " ".join(single_words))