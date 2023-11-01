def do_stuff_with_number(n):
    print(n)

# chúng ta sử dụng try-except block để bắt lỗi IndexError được ném ra
# khi chúng ta cố gắng truy cập vào một phần tử không tồn tại trong danh sách.
def catch_this():
    the_list = (1, 2, 3, 4, 5)
    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:
            do_stuff_with_number(0)

catch_this()
