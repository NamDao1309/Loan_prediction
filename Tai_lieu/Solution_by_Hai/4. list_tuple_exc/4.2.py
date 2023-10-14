# 4.2
list1 = ["M", "na", "i", "Peter"]
list2 = ["y", "me", "s", "Parker"]
# list3 = [i + j for i, j in zip(list1, list2)]
list3 = []
for i, j in zip(list1, list2):
    list3.append(i + j)
print(list3)
