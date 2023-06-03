#!/usr/bin/python3

def uppercase(str):
    upper = ''
    for sentence in str:
        if 97 <= ord(sentence) <= 122:
            upper = upper + chr(ord(sentence) - 32)
        else:
            upper = upper + sentence

    print("{}".format(upper))
