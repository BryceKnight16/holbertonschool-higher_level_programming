#!/usr/bin/python3
'''
Module that has append method
'''


def append_write(filename="", text=""):
    '''
    a function that appends the text in the filename and adds it to the
    end of the file

    Args:
    filename(str): the filename to be written in
    text(str): the text to be written in the file

    Return:
    appended_file wit new text at the end of file
    '''

    with open(filename, 'a', encoding="utf-8") as f:
        appended_file = f.write(text)
        return appended_file
