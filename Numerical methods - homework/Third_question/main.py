from Third_question.function import func
from function import function1
from bisection_method import Bisection

method = Bisection(func)
print(method.finder(-2, 1, 0.0001))