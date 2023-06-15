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

     new_dict = dict(a_dictionary)
    for key in a_dictionary:
        new_dict[key] = new_dict[key] * 2
    return new_dict

