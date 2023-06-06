#!/usr/bin/python3

def no_c(my_string):
    my_new_string = my_string.translate( {ord("C"): None})
    my_new_new_string = my_new_string.translate( {ord("c"): None})
    return(my_new_new_string)
