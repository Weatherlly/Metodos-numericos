import numpy as np
import math

def radius_location_1(coeff):
    vet_coeff = []
    for coeff in coeff:
        if (coeff != 0):
            vet_coeff.append(coeff)
    n = len(vet_coeff) - 1
    aux1 = n*abs(vet_coeff[0]/vet_coeff[1])
    aux2 = (abs(vet_coeff[0]/vet_coeff[-1]))**(1/n)
    r1 = min([aux1, aux2])
    return r1


def radius_location_2(vet_coeff):
    vref = 0
    for i in range(0, len(vet_coeff) - 1):
        if abs(vet_coeff[i]/vet_coeff[-1]) > vref:
            vref = abs(vet_coeff[i]/vet_coeff[-1])
    return 1+vref