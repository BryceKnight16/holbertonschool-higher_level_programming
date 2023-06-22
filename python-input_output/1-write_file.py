#!/usr/bin/python3
'''
Module that has a write file funciton
'''


def write_file(filename="", text=""):
    '''
    a function that write the text in the filename

    Args:
    filename(str): the filename to be written in 
    text(str): the text to be written in the file

    Return:
    the number of chars in written_file
    '''

    with open(filename, 'w', encoding="utf-8") as f:
        written_file= f.write(text)
        return written_file
