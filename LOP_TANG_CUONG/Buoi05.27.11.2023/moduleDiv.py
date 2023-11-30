def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Không thể chia cho 0")