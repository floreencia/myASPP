# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math

def test_arithmetic():
    assert 1 == 1
    assert 2 * 3 == 6
    
def test_len_list():
    lst = ['a', 'b', 'c']
    assert len(lst) == 3
    
def test_one_plus_two_is_three():
    assert 1 + 2 == 3
    
def test_sum():
    assert math.isclose(1.1 + 2.2, 3.3)
    
def test_nparrays():
    x = np.array([1, 1])
    y = np.array([2, 2])
    z = np.array([3, 3])
    assert (x + y == z).all()