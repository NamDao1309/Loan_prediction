#Dictionary
dictFruit = {
    1: 'Apple',
    2: 'Banana',
    3: 'Mango',
    4: 'Kiwi'
}

print(dictFruit[1])
print(dictFruit[2])
print(dictFruit)

#bài tập 1
aList = [1,2,3,4,5,6,7]
for i in range(0,len(aList)):
    aList[i] = int(aList[i])**2
print(aList)

#bai tap 2
list1 = ["M", "na", "i", "Peter"]
list2 = ["y", "me", "s", "Parker"]
lisTT = ['d','f','h','i']
for i in range(0,4):
    lisTT[i] = list1[i] + list2[i]
print(lisTT)

#bai tap 3
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
lisVV = []
for i in range(0,2):
    for y in range(0,2):
        lisVV.append(list1[i] + list2[y])
print(lisVV)

#bai tap 4
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i == 20:
        list1.remove(20)
print(list1)

#bai tap 5
# file_name = 'romeo.txt'
# with open("D:\python project\GITHUB\VIETECH\VIETECH_DA_28.09.2023\Student's homeworks\Do Quang Trung\romeo.txt", "r") as f:
#     lines = f.read()
#     print(lines)

    




