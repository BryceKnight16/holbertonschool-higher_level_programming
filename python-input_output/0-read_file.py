#!/usr/bin/python3
'''
A module 0-readfile made it read files and print tot he standard
Output
'''


def read_file(filename=""):
    '''
    Read file adn print to stdout

    Args:
    filename(str): Name of file to be read

    Returns:
    None

    '''

    with open(filename, 'r', encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end='')
