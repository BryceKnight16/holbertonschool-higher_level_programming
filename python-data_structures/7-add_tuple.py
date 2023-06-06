#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_zero = (0, 0)
    n_tup_a = tuple_a + tup_zero
    n_tup_b = tuple_b + tup_zero

    n_tuple = ((n_tup_a[0] + n_tup_b[0]), (n_tup_a[1] + n_tup_b[1]))
    return(n_tuple)
