#!/usr/bin/python3
'''
Module that has a write file funciton
'''


def write_file(filename="", text=""):
    '''
    a function that write the text in the filename
    '''

    with open(filename, 'w', encoding="utf-8") as f:
        written_file= f.write(text)
        return written_file
