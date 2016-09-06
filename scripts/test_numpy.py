# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:03:03 2016

@author: student
"""
import numpy as np
from numpy.testing import assert_array_almost_equal

def test_numpy_var():
    
    var = 1
    mean = 1
    test_cases=[
                (np.ones(10).var(), 0),
                (np.random.randn(10)*var + mean, var)
                ]
    
    for test, expected in test_cases:    
        assert_array_almost_equal(test, expected)