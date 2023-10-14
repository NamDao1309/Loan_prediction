# 4.4
# del all 20 value
list6 = [5, 20, 15, 20, 25, 50, 20]
# list6 = [i for i in list6 if i != 20]

while (20 in list6):
    list6.remove(20)
print(list6)