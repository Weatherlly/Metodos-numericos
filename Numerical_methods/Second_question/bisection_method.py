def bisection(l, h, function, accuracy = 0.01, maxiter = 50):
    niter = 0
    fxl = function(l)
    fxh = function(h)

    x_estim, fx_estim, error, niter = p_unit(l, h, niter, function)
    while (niter < maxiter) and ( error > accuracy):
        if (fxl * fx_estim > 0) and (fxh * fx_estim > 0):
            print("Incorrect choice of estimates")
            return 0
        if fxl * fx_estim < 0:
            h = x_estim
            fxh = function(h)
        else:
            if fx_estim == 0:
                return x_estim
            l, x_estim
            fxl = function(l)
        x_estim, fx_estim, error, niter = p_unit(l, h, niter, function)
    return x_estim

def p_unit(l, h, niter, function):
    x_estim = (l + h)/2
    fx_estim = function(x_estim)
    error = abs((x_estim - l)/x_estim)
    niter += 1
    return x_estim, fx_estim, error, niter