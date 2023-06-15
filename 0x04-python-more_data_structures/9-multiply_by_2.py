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

     new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *= 2

    return (new_dir)

