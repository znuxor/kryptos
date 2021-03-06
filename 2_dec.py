#!/usr/bin/env python3
''' decrypts the first passage'''
from Vigenere import Vigenere

keyword_1 = 'kryptos'
keyword_2 = 'abscissa'

with open('text_a.txt', 'r') as f:
    text = f.read().replace('\n', '').lower()

key_1 = 'betweensubtleshadingandtheabsenceoflightliesthenuanceofiqlusion'
text = text[len(key_1):].replace('?', '')

print(text)

my_decriptor_1 = Vigenere(keyword_1, keyword_2)
text_dec = my_decriptor_1.decrypt(text)
print(text_dec)
