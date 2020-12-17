class calc:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        res = self.x + other
        return res

    def __mul__(self, other):
        res = self.x * other
        return res

    def __sub__(self, other):
        res = self.x - other
        return res
