import os
import csv
import re

words = []
sentences = []


txtpath = os.path.join('paragraph_1.txt')
with open(txtpath) as txtfile:
    paragraph = txtfile.read()


    words = paragraph.split(" ")
    word_count = len(words)
    total_letters = sum(len(word) for word in words)
    letter_count =  total_letters / word_count

    sentences = len(re.split("(?<=[.!?]) +", paragraph))
    sentence_length = word_count / sentences

print("Paragraph Analysis")
print("------------------------")
print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(sentences))
print("Average Letter Count: " + str(round(letter_count,2)))
print("Average Sentence Length: " + str(round(sentence_length,2)))