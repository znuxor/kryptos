#!/usr/bin/env python3
''' decrypts the first passage'''
from Vigenere import Vigenere

keyword_1 = 'kryptos'
keyword_2 = 'abscissa'

with open('text_b.txt', 'r') as f:
    text = f.read().replace('\n', '').lower()

text = text[:text.index('?')]
# cut into 14x24 matrix
matrix = []
for i in range(14):
    matrix.append(list(text[i*24:(i+1)*24]))

# rotate
matrix = zip(*matrix[::-1])

# restring it
text = ''
for line in matrix:
    text += ''.join(line)

# cut into 42x8 matrix
matrix = []
for i in range(42):
    matrix.append(list(text[i*8:(i+1)*8]))

# rotate
matrix = zip(*matrix[::-1])

# restring it
text = ''
for line in matrix:
    text += ''.join(line)

print(text)
