class Bisection:
    def __init__(self, func):
        self.func = func

    def finder(self, l, h, accuracy = 0.01, maxiter = 50):
        niter = 0
        fxl = self.func(l)
        fxh = self.func(h)

        x_estim, fx_estim, error, niter = self.p_unit(l, h, niter)
        while (niter < maxiter) and (error > accuracy):
            if (fxl * fx_estim > 0) and (fxh * fx_estim > 0):
                print("Incorrect choice of estimates:")
                return 0
            if fxl * fx_estim < 0:
                h = x_estim
                fxh = self.func(h)
            else:
                if fx_estim == 0:
                    return x_estim
                l = x_estim
                fxl = self.func(l)
            x_estim, fx_estim, error, niter = self.p_unit(l, h, niter)
        print("Total iterations:", niter)
        return x_estim

    def p_unit(self, l, h, niter):
        x_estim = (l + h)/2
        fx_estim = self.func(x_estim)
        error = abs((x_estim - l)/x_estim)
        niter += 1
        return x_estim, fx_estim, error, niter