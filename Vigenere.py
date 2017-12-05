#!/usr/bin/env python3
''' Contains an homemade vigenere module'''
from collections import deque
from copy import deepcopy


class Vigenere():
    '''A vigenere decoding class'''
    def __init__(self, horizontal_key, vertical_key):
        # save the key
        self.horizontal_keyword = horizontal_key
        self.vertical_keyword = vertical_key
        # generate the complete vigenere table
        base_row = ''.join(list(chr(ord('a')+i) for i in range(26)))
        for a_char in self.horizontal_keyword:
            base_row = base_row.replace(a_char, '')
        base_row = deque(self.horizontal_keyword + base_row)

        vigenere_table = []
        self.row_meaning = deepcopy(base_row)

        for a_char in self.vertical_keyword:
            base_row.rotate(-base_row.index(a_char))
            vigenere_table.append(deepcopy(base_row))

        self.table = deepcopy(vigenere_table)

    def decrypt(self, text):
        '''decrypts the text and returns it'''
        decrypted_text = deque()
        key_len = len(self.vertical_keyword)
        for index, a_char in enumerate(text):
            try:
                decrypted_text.append(
                    self.row_meaning[self.table[index % key_len].index(a_char)]
                    )
            except ValueError:
                decrypted_text.append(a_char)
        return ''.join(decrypted_text)
