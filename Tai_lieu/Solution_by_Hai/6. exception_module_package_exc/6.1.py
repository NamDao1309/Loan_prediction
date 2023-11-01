actor = {"name": "John Cleese", "rank": "awesome"}

# Trong trường hợp này, chúng ta bắt lỗi `KeyError` được ném ra khi
# chúng ta cố gắng truy cập vào một khóa không tồn tại trong từ điển.
def get_last_name():
    try:
        return actor["last_name"]
    except KeyError:
        return None

get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
