"""
This is going to be an attempt to turn information from the textbook on 
compuatational techniques by Giordano and Naakanishi (2005)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# focus on getting code down now and I can implement OOP later

# OOP work

# 1.1 Radioactive Decay

# functions

# 1.1 Radioactive Decay

## What is a taylor expansion?

def dt_u235():
    """
    this time step can be used for the radioactive decay
    no inputs for the moment it should just return a time? idk
    """
    t = np.linspace(1,100, 100)
    print(t)
    return t

def u_235_decay(n,t, gamma):
    """
    Args:
        n (int): # of u235 nuclei present in sample
        t (float): time  
        gamma (float?): "time constant" for the decay
    """
    # the recursion idea came from gpt so this might not account for 
    # all the information
    
    # recursive base case
    if n <= 0 or t <= 0:
        return 0 
    
    decayed_nuclei = n*(1 - gamma)
    remaining_nuclei = u_235_decay(decayed_nuclei, (t-1), gamma)
    
    return decayed_nuclei + remaining_nuclei

