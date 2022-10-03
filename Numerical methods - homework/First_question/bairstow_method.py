import numpy as np
import math


def bairstow_method(vet_coeff, r, s, grade, epsilon):
    xx = np.linspace(0, grade, grade + 1)
    bi = []
    ci = []
    roots = []
    for x in xx:
        bi.append(0)
        ci.append(0)
        roots.append(0)
    id_root = 0
    while grade >= 3:
        igrade = grade
        bi[igrade] = vet_coeff[igrade]
        while igrade > 0:
            igrade = igrade - 1
            if igrade == grade - 1:
                bi[igrade] = vet_coeff[igrade] + r * bi[igrade + 1]
            else:
                bi[igrade] = vet_coeff[igrade] + \
                    r * bi[igrade + 1] + s * bi[igrade + 2]
        igrade = grade
        ci[igrade] = bi[igrade]
        while igrade > 1:
            igrade = igrade - 1
            if igrade == grade - 1:
                ci[igrade] = bi[igrade] + r * ci[igrade + 1]
            else:
                ci[igrade] = bi[igrade] + r * \
                    ci[igrade + 1] + s * ci[igrade + 2]
        ds = (bi[1] * (ci[1]/ci[2]) - bi[0])/(ci[2] - (ci[1]/ci[2]) * ci[3])
        dr = (-1 * bi[1] - ci[3] * ds)/ci[2]
        r = r + dr
        s = s + ds

        while abs(dr/r) > epsilon or abs(ds/s) > epsilon:
            igrade = grade
            bi[igrade] = vet_coeff[igrade]
            while igrade > 0:
                igrade = igrade - 1
                if igrade == grade - 1:
                    bi[igrade] = vet_coeff[igrade] + r * bi[igrade + 1]
                else:
                    bi[igrade] = vet_coeff[igrade] + \
                        r * bi[igrade + 1] + s * bi[igrade + 2]
            igrade = grade
            ci[igrade] = bi[igrade]
            while igrade > 1:
                igrade = igrade - 1
                if igrade == grade - 1:
                    ci[igrade] = bi[igrade] + r * ci[igrade + 1]
                else:
                    ci[igrade] = bi[igrade] + r * \
                        ci[igrade + 1] + s * ci[igrade + 2]
            ds = (bi[1] * (ci[1]/ci[2]) - bi[0]) / \
                (ci[2] - (ci[1]/ci[2]) * ci[3])
            dr = (-1 * bi[1] - ci[3] * ds)/ci[2]
            r = r + dr
            s = s + ds

        print('The values ​​found for r and s are respectively: %f, %f' % (r, s))
        d = r**2+4*s
        if d > 0:
            roots[id_root] = (r + math.sqrt(d))/2
            ''' print("Root = ", roots[id_root]) '''
            id_root = id_root + 1
            roots[id_root] = (r - math.sqrt(d))/2
            ''' print("Root = ", roots[id_root]) '''
            id_root = id_root + 1

        else:
            roots[id_root] = (r + complex(0, math.sqrt(-1 * d)))/2
            ''' print("Root = ", roots[id_root]) '''
            id_root = id_root + 1
            roots[id_root] = (r - complex(0, math.sqrt(-1 * d)))/2
            ''' print("Root = ", roots[id_root]) '''
            id_root = id_root + 1

        grade = grade - 2
        igrade = grade
        while igrade >= 0:
            vet_coeff[igrade] = bi[igrade + 2]
            igrade = igrade - 1
    if grade == 2:
        d = vet_coeff[1]**2-4 * \
            vet_coeff[2] * vet_coeff[0]
        if d >= 0:
            roots[id_root] = (-1 * vet_coeff[1] +
                              math.sqrt(d))/(2 * vet_coeff[2])
            ''' print("Root = ", roots[id_root]) '''
            id_root = id_root + 1
            roots[id_root] = (-1 * vet_coeff[1] -
                              math.sqrt(d))/(2 * vet_coeff[2])
            ''' print("Root = ", roots[id_root]) '''
            id_root = id_root + 1

        else:
            roots[id_root] = (-1 * vet_coeff[1] + complex(0,
                              math.sqrt(-1 * d)))/(2 * vet_coeff[2])
            ''' print("Root = ", roots[id_root]) '''
            id_root = id_root + 1
            roots[id_root] = (-1 * vet_coeff[1] - complex(0,
                              math.sqrt(-1 * d)))/(2 * vet_coeff[2])
            ''' print("Root = ", roots[id_root]) '''
            id_root = id_root + 1
    else:
        roots[id_root] = (-1 * vet_coeff[0])/vet_coeff[1]
        ''' print("Root = ", roots[id_root]) '''
    roots.pop()
    return [-root for root in roots]
