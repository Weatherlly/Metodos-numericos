import numpy as np
import math

def root_estimator(vet_coeff):
    var = 0
    i = 0
    j = 1
    while i < len(vet_coeff)-1 and j < len(vet_coeff):
        if vet_coeff[i]*vet_coeff[j] < 0:
            var += 1
            i = i+1
            j = j+1
        elif vet_coeff[i]*vet_coeff[j] == 0:
            if vet_coeff[j] == 0:
                j = j+1
            else:
                i = i+1
        else:
            i = i+1
            j = j+1

    positive_roots = []
    for i in range(0, var+1):
        if (var - i) % 2 == 0:
            positive_roots.append(i)

    var = 0
    i = 0
    j = 1
    for k in range(0, len(vet_coeff)):
        vet_coeff[k] = vet_coeff[k]*((-1)**k)

    while i < len(vet_coeff)-1 and j < len(vet_coeff):
        if vet_coeff[i]*vet_coeff[j] < 0:
            var += 1
            i = i+1
            j = j+1
        elif vet_coeff[i]*vet_coeff[j] == 0:
            if vet_coeff[j] == 0:
                j = j+1
            else:
                i = i+1
        else:
            i = i+1
            j = j+1

    negative_roots = []
    for i in range(0, var+1):
        if (var - i) % 2 == 0:
            negative_roots.append(i)

    complex_roots = []
    grade = len(vet_coeff)-1
    for i in positive_roots:
        for j in negative_roots:
            complex_roots.append(grade - i - j)

    return positive_roots, negative_roots, complex_roots