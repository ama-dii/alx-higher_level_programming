#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    function that returns a new dictionary with all values multiplied by 2
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary

    Return:
        a new dictionary
    """

    return ({c: a_dictionary[k] * 2 for c in a_dictionary})

