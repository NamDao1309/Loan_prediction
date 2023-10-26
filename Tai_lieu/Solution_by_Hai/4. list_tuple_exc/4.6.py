# 4.6
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Chuyển số sang chữ
def num_to_word(num):
    if (num == 0):
        return 'không'
    elif (num == 1):
        return 'một'
    elif (num == 2):
        return 'hai'
    elif (num == 3):
        return 'ba'
    elif (num == 4):
        return 'bốn'
    elif (num == 5):
        return 'năm'
    elif (num == 6):
        return 'sáu'
    elif (num == 7):
        return 'bảy'
    elif (num == 8):
        return 'tám'
    elif (num == 9):
        return 'chín'

for i in n:
    print(num_to_word(i), end=' ')
