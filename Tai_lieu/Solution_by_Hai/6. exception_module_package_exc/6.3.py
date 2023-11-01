# chúng ta sử dụng try-except block để bắt lỗi NameError được ném ra
# khi chúng ta cố gắng truy cập vào một biến không tồn tại.

try:
    print(a)
except NameError:
    print("Variable 'a' is not defined!")
