def count_word_frequency(input_file, output_file):
    word_frequency = {}

    # Đọc nội dung của file input
    with open(input_file, "r") as file:
        content = file.read()

    # Tách các từ trong nội dung
    words = content.split()

    # Đếm tần số xuất hiện của từng từ
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Ghi kết quả vào file output
    with open(output_file, "w") as file:
        for word, frequency in word_frequency.items():
            file.write(f"{word}: {frequency}\n")

input_file = "input_3.txt"
output_file = "output_3.txt"
count_word_frequency(input_file, output_file)