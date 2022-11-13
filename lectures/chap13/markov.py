"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import sys
import string
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename, encoding='utf8')
    skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END'): 
            break

        for word in line.rstrip().split():
            process_word(word, order)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START'):
            break


def process_word(word, order=2):
    """Processes each word.

    word: string
    order: integer

    During the first few iterations, all we do is store up the words; 
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)

def capitalized_prefix():
    keys = list(suffix_map.keys())
    start = random.choice(keys)
    while start[0][0] not in string.ascii_uppercase:
        start = random.choice(keys)
    return start


def random_text(n=100):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = capitalized_prefix()
    chars = 0
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        chars += len(start[0]) + 1
        print(start[0], end=' ')
        if chars > 50:
            print()
            chars = 0
        word = random.choice(suffixes)
        start = shift(start, word)
    for i in range(1,len(start)):
        print(start[i], end=' ')
    print()

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main(filename='tarzanoftheapes.txt', n=128, order=2):
    print('File:', filename.split('/')[-1])
    print()
    print('Order:', order)
    print()
    process_file(filename, order)
    random_text(n)
        
from tkinter import filedialog, simpledialog
from tkinter import *

root = Tk()
root.withdraw()
filename =  filedialog.askopenfilename(title = "Select file:",filetypes = (("text files","*.txt"),("all files","*.*")))
order = simpledialog.askinteger(title="Set order", prompt="order:")
main(filename, 100, order)
