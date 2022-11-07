import numpy as np
import math
from bairstow_method import bairstow_method
from radius import radius_location_1, radius_location_2
from root_estimator import root_estimator

radius = 10
accuracy = 0.0001
vet_poly = [[-20, 3, 14.5, -7.5, 1],
                    [10, -7, -6, 1, -5, 1],
                    [-5, -3, 1, 1],
                    [-3, 4, -0.5, 1],
                    [10, 0, 6, 0, 2],
                    [8, -8, 6, -2, 1]]

for poly in vet_poly:
    grade = len(poly) - 1

    print("\n===================================================================")
    print("f(x) = ", end="")
    for index, coeff in enumerate(poly):
        if (index == grade):
            print("{}.x^({})".format(coeff, index))
            continue
        print("{}.x^({}) + ".format(coeff, index), end="")

    positives, negatives, complexs = root_estimator(poly)
    print("Positives roots: {}".format(positives))
    print("Negatives roots: {}".format(negatives))
    print("Complexs roots: {}".format(complexs))
    print("The radius that has all the roots = ", radius_location_2(poly))
    print("The Roots are: ")
    roots = bairstow_method(poly, radius, -radius, grade, accuracy)
    for index, root in enumerate(roots):
        print("Root {} = {}".format(index+1, root))