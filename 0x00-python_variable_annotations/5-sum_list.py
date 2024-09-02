#!/usr/bin/env python3
""" type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        sum_list takes a list input_list of floats as argument and
        returns their sum as a float.
    """
    sum: float = 0.0
    for value in input_list:
        sum = value + sum

    return sum
