# 4.5
unique_words = []

with open('romeo.txt', 'r') as file:
    for line in file:
        words = line.split()

        for word in words:
            if word not in unique_words:
                unique_words.append(word)

        # xóa ký tự thừa khác trong từ
        for word in unique_words:
            if (word[-1] in [',', '.', '?', '!', ':', ';', '"', "'", '-', '_', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '`', '~', '@', '#', '$', '%', '^', '&', '*', '+', '=']):
                unique_words[unique_words.index(word)] = word[:-1]
            if  (word[1] in [',', '.', '?', '!', ':', ';', '"', "'", '-', '_', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '`', '~', '@', '#', '$', '%', '^', '&', '*', '+', '=']):
                unique_words[unique_words.index(word)] = word[1:]
unique_words.sort()

for word in unique_words:
    print(word)
