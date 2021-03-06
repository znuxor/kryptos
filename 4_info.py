#!/usr/bin/env python3
''' decrypts the fourth passage'''

clue = 'berlinclock'
clue_pos = 63

with open('text_b.txt', 'r') as f:
    text = f.read().replace('\n', '').lower()

text = text[text.index('?')+1:]
print('text:')
print(text)
print('Number of characters: ', end='')
print(len(text))
for i in range(26):
    letter = chr(ord('a')+i)
    print('{}: '.format(letter), end='')
    print(text.count(letter))
