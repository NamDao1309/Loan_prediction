# 2. from/from*
from exception_module_package_exc import myclient
from mypkg.mymod import countLines, countChars, test

file_path = 'data_for_mymod.txt'

with open(file_path) as f:
    countLines(file_path)
    countChars(file_path)
    test(file_path)

# 4. nested imports
print(myclient.__dict__)

# 7. [Optional] Circular imports hay còn gọi là "nhập chéo"

# Trong Python, khi 2 hay nhiều module cố gắng nhập lẫn nhau một cách trực tiếp hoặc gián tiếp, ta gặp phải hiện tượng nhập chéo này.
#
# 1. Việc nhập `recur1` gây ra lỗi:
#    Khi nhập `recur1`, nó thực thi mã trong `recur1.py` từ trên xuống dưới
#    Nếu `recur1` cố gắng nhập `recur2` trước khi `recur2` được định nghĩa hoàn toàn, lỗi sẽ xảy ra vì `recur2` chưa có sẵn trong không gian tên
#    Đây là một vấn đề phổ biến của hiện tượng nhập chéo
#    Python thực thi mã tuần tự và nó không biết về nội dung của module cho đến khi hoàn thành việc thực thi nó
#
# 2. Việc nhập `recur2` theo cách tương tác không gây lỗi:
#    Khi nhập `recur2` theo cách tương tác sau khi khởi động lại Python, lỗi không xảy ra vì Python lưu trữ các module trong từ điển `sys.modules`
#    Một khi module được nhập, tham chiếu của nó được lưu trữ trong `sys.modules`
#    Khi nhập `recur2` theo cách tương tác, Python tìm thấy nó trong `sys.modules` và trả về module đã được nhập trước đó, bất kể module đã hoàn thành việc thực thi hay chưa
#    -> Hành vi này cho phép nhập chéo hoạt động mà không gây lỗi.
#
# 3. Chạy `recur1.py` như một tệp script:
#    Khi chạy `recur1.py` như một tệp script bằng `% python recur1.py`, nó hoạt động tương tự như việc nhập `recur2` theo cách tương tác
#    Tệp script được thực thi từ đầu đến cuối, giống như việc nhập, và module `recur2` được tìm thấy trong `sys.modules`, cho phép nhập chéo hoạt động mà không gây lỗi
#
# 4. Chạy `recur2` như một tệp script:
#    Khi chạy `recur2.py` như một tệp script bằng `% python recur2.py`, nó không gây ra bất kỳ lỗi nào vì `recur2` không cố gắng nhập `recur1`
#    Vì `recur1` không được nhập hoặc thực thi, vấn đề nhập chéo được tránh
#
# Tóm lại, cơ chế lưu trữ trong `sys.modules` của Python cho phép nhập chéo hoạt động mà không gây lỗi khi các module được nhập hoặc thực thi như tệp script.
# Tuy nhiên, cần cẩn trọng khi làm việc với nhập chéo, vì nó vẫn có thể gây ra lỗi.


