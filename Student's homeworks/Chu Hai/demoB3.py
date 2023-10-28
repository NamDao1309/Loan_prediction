#bài tập vòng lặp while
#sự khác nhau giữa break và continue

# i= 0
# while(i<5):
#     if(i==3):
#         break
#     i=i+1
#     print(i)
#hamf range
# for x in range(9):
#     print(x)
# tổng số nguyên 1-100 sử dụng for/range
# S=0
# for i in range(1,101,):
#  S += i
#  print(S)


########### in ra bảng cửu chương
for i in range(1, 10):
    for j in range(1, 10):
        F = i * j
        print(f"{i} x {j} = {F}")
    print() 