from functions import function1, function2
from bisection_method import bisection
from root_calculator import root_calculator

print("Function of item A")
print("The roots are = ", root_calculator(-100, 100, function1, bisection, 10000))
print("\n")
print("Function of item B")
print("The roots are = ", root_calculator(0.1, 100, function2, bisection, 10000))