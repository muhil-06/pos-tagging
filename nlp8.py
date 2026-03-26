import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


text = "Artificial intelligence is transforming the world. Machine learning helps computers learn from data."


words = word_tokenize(text)

pos_tags = pos_tag(words)

print("POS Tags:")
for word, tag in pos_tags:
    print(word, ":", tag)