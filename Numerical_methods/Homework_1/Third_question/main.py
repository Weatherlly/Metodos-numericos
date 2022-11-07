from function import func
from bisection_method import Bisection

method = Bisection(func)
print(method.finder(-2, 1, 0.0001))