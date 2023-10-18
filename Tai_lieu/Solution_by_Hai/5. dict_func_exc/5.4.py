# 5.4


def outer_func(a, b):
    def addition(c, d):
        return c + d
    return addition(a, b) + 5


print(outer_func(10, 20))