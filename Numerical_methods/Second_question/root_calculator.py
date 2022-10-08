import numpy as np

def root_calculator(i, f, function, method, breaker = 1000):
    breaks = finder(i, f, function, breaker)
    print("Range list = ", breaks)
    return caller(breaks, function, method)

def finder(i, f, function, breaker):
    aspirants = np.linspace(i, f, breaker)

    possible_zeros = []
    size = len(aspirants)
    gap = (i - f)/breaker

    for index, elements in enumerate(aspirants):
        if (function(elements) * function(elements + gap) < 0):
            possible_zeros.append([elements, elements + gap])
        if (index == size):
            continue
    return possible_zeros

def caller(range_list, function, method):
    roots = []

    for lower, higher in range_list:
        roots.append(method(lower, higher, function))

    return roots