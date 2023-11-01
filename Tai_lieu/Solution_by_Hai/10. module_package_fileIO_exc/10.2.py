# Đọc nội dung của file input.txt
with open("input_2.txt", "r") as file:
    content = file.read()

# Tách các từ trong nội dung
words = content.split()

# Tìm từ có độ dài lớn nhất
max_length = 0
max_word = ""

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        max_word = word

# In kết quả
print(f"Từ {max_word} có độ dài {max_length} ký tự")
