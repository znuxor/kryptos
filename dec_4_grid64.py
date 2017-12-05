#!/usr/bin/env python3
''' decrypts the fourth passage'''
from functools import reduce
from copy import deepcopy


def generate_factors(n):
    ''' returns the factors of a number'''
    return (
        reduce(list.__add__,
               ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def verify(text):
    clue = 'berlinclock'
    clue_pos = 63
    return clue == text[clue_pos:clue_pos+len(clue)]


def rotate(p_text, row_number, col_number):
    ''' returns a rotate string'''
    # cut into matrix
    matrix = []
    for row_num in range(row_number):
        matrix.append(list(p_text[row_num*col_number:(row_num+1)*col_number]))
    # rotate
    matrix = zip(*matrix[::-1])

    # restring
    ret_text = ''
    for line in matrix:
        ret_text += ''.join(line)
    return ret_text


def recursive_rotate(ptext, remaining_combos):
    ''' Returns a list of all possible rotate tree results'''
    rotated_texts = []
    for i, a_combo in enumerate(remaining_combos):
        work_text = deepcopy(ptext)
        work_text = rotate(work_text, a_combo[0], a_combo[1])
        rotated_texts.append(deepcopy(work_text))
        rotated_texts.extend(recursive_rotate(
            work_text, remaining_combos[:i]+remaining_combos[i+1:]))

        # reversed combo
        work_text = deepcopy(ptext)
        work_text = rotate(work_text, a_combo[1], a_combo[0])
        rotated_texts.append(deepcopy(work_text))
        rotated_texts.extend(recursive_rotate(
            work_text, remaining_combos[:i]+remaining_combos[i+1:]))
    return rotated_texts


# start of script

with open('text_b.txt', 'r') as f:
    text = f.read().replace('\n', '').lower()

text = text[text.index('?')+1:]
passage_text = text
char_number = len(passage_text)
print(len(text))
print('boop')
for i in range(23+1):
    remaining_chars = i
    text = passage_text[:char_number-remaining_chars+1+1]
    chars_in_text = len(text)

    the_factors = generate_factors(chars_in_text)
    if len(the_factors) == 2:
        continue

    # remove the blegh factors (1 and the number)
    the_factors = the_factors[2:]

    # find the matrix rotation combos
    combos = []
    for j in range(len(the_factors)//2):
        combos.append(the_factors[2*j:2*(j+1)])


    my_texts = recursive_rotate(text, combos)
    print(len(my_texts))
    print(chars_in_text)
    for a_text in my_texts:
        if verify(a_text):
            print("success!")
