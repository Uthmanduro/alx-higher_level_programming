#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence = None
        return (0, sentence)
    first_char = sentence[0]
    return (len(sentence), first_char)
