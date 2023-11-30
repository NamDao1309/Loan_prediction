import matplotlib.pyplot as plt 
import numpy as np
from numpy.random import randn
import math
import matplotlib.image as ming
#tao khung hinh
# fig = plt.figure()

# create 1 or many subplot 
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)

# ax1.plot(np.arange(0.0, 5.0, 0.2), 'r--')
# ax2.plot(randn(50).cumsum(), 'g--')
# ax3.plot(np.sin(np.arange(0, 3*np.pi, 0.1)))
# ax4.plot(1.5, 3.5, -2, 1.6, 'b*')
# 
# fig , axes = plt.subplots(2,3)
# axes[0,1].plot(randn(50).cumsum(), color='g', linestyle= 'dashed', marker='')
# axes[1,1].hist(randn(100), bins = 20, color= 'k', alpha = 0.3)
# axes[0,2].scatter(np.arange(30), np.arange(30) + 3*randn(30))

#  dung for de ve
# fig, axes = plt.subplot(2,2, sharex= True , sharey = True)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(randn(500), bins = 50, color='g', alpha = 0.5)
# plt.show() (wrong)

# Tiks, Labels, Legends
#Vẽ đồ thị hình sin
# x = np.arange(0, math.pi*2, 0.05)
# y = np.sin(x)

# axes = plt.axes()
# plt.xlabel("Trục x")
# plt.ylabel("Trục y")

# plt.title("Biểu diễn đồ thị hình sin")
# plt.plot(x,y, color='b')
# # set sticker
# axes.set_xtick([0,2,4,6])
# axes.set_ytick([-1,0,1])
# #set lable tick
# axes.set_yticklabels(["sin(-90)","sin(0)","sin(90)"])
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import math

x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

plt.xlabel("Trục x")
plt.ylabel("Trục y")

plt.title("Biểu diễn đồ thị hình sin")
plt.plot(x,y, color='b')
# set sticker
plt.xticks([0,2,4,6])
plt.yticks([-1,0,1], ["sin(-90)","sin(0)","sin(90)"])

path_image =
image= ming.imread(path_image)
x= np.arange(0,math.pi*3,0.1)
y = np.sin(x)
fig, axes = plt.subplot(2,2, figsize =(5,5))

# plt.savefig(r'D:\DA\VIETECH_DA_28.09.2023\Student\'s homeworks\Chu Hai\buoi17.png')

# plt.show()


# Vẽ cả 2 đồ thị hình Sin và Cos

# x = np.arange(0, math.pi*2, 0.05)
# y = np.sin(x)
# z = np.cos(x)
# axes=plt.axes()
# fig, axes = plt.subplot(2,2)

# plt.xlabel("truc x")
# plt.ylabel("truc y")
# plt.title("bieu do hinh sin")

# axes[0,1].plot(x,y,color='b')
# axes[0,2].plot(x,z,color='r')
# # axes_sin = plt.axes[0,1]

# ve do thi y=x^2]
# x = np.linspace(-5, 5, 100)  # Tạo một dãy điểm từ -5 đến 5
# y = x**2  # Tính giá trị y tương ứng với mỗi giá trị x

# plt.plot(x, y)  # Vẽ đồ thị y = x^2
# plt.xlabel('x')  # Đặt nhãn trục x
# plt.ylabel('y')  # Đặt nhãn trục y
# plt.title('Đồ thị của hàm y = x^2')  # Đặt tiêu đề của đồ thị
# plt.grid(True)  # Hiển thị lưới đồ thị


plt.show()  # Hiển thị đồ thị


#sin, cos trong cùng 1 plot (slide)
#x = np.arange(0, 3*np.pi, 0.1)
# y = np.sin(x)
# z = np.cos(x)