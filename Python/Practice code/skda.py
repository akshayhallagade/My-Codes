import math


class Solver:
    def roots(self):
        a = 3
        b = 25
        c = 46
        root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return root1, root2


Solver().demo()
