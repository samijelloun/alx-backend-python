#!/usr/bin/env python3
"""
    type-annotated function concat that takes a string str1 and a string str2
    as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """ concat fuction returns a concatenated string composed of
        str1 and str2
    """
    return str(str1 + str2)
