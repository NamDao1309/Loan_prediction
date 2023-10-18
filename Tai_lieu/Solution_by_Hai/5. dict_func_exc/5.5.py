# 5.5


def sum(n):
    return sum(n - 1) + n if n > 0 else 0
    # if (n == 0):
    #     return 0
    # else:
    #     return sum(n - 1) + n


print(sum(10))