# -*- coding: utf-8 -*-

"""Main module."""

def is_pangram(sentence):
    """Determines if a sentence is a pangram."""
    from string import ascii_lowercase
    sentence = sentence.lower()
    for letter in ascii_lowercase:
        if letter not in sentence: # if some letter from English alphabet is not used in given sentence
            return False
    return True