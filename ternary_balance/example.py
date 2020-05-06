"""Example program to use the solver.
"""

from ternary_balance.solver import ternary_balance

solver = ternary_balance()

m = 3

for _ in range(3):
    solver.solve()
