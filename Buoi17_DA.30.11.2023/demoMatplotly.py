import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import math
import matplotlib.image as mpimg


# tao khung hinh
#fig = plt.figure()

# create 1 or many subplot
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)

# ax1.plot(np.arange(0.0, 5.0, 0.2), 'r--')
# ax2.plot(randn(50).cumsum(), 'g--')
# ax3.plot(np.sin(np.arange(0, 3*np.pi, 0.1)))
# ax4.plot([1.5, 3.5, -2, 1.6], 'b*')

# fig, axes = plt.subplots(2,3)
# axes[0,1].plot(randn(50).cumsum(), color='g', linestyle='dashed', marker='+')
# axes[1,1].hist(randn(100), bins = 20, color='k', alpha = 0.3 )
# axes[0,2].scatter(np.arange(30), np.arange(30) + 3*randn(30))

# dung for de ve
#fig, axes = plt.subplots(2,2, sharex=True , sharey= True)
# fig, axes = plt.subplots(2,2)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(randn(500), bins = 50, color='g', alpha = 0.5)

#plt.subplots_adjust(wspace=1, hspace=1)

# TICKS, LABELS, LEGENDS
# VẼ ĐỒ THỊ HÌNH SIN
# x = np.arange(0, math.pi*2, 0.05)
# y = np.sin(x)

# axes = plt.axes()
# plt.xlabel("Trục x")
# plt.ylabel("Trục y")

# plt.title("Biểu diễn đồ thị hình sin")
# plt.plot(x, y, color='b')

# # set ticker cho trục x, y
# axes.set_xticks([0, 2, 4, 6])
# axes.set_yticks([-1, 0, 1])
# # set label tick or y tick
# axes.set_yticklabels(["sin(-90)", "sin(0)", "sin(90)"])
# # save figure
# plt.savefig('VIETECH_DA_28.09.2023//Buoi16_DA.25.11.2023//chart_sin.png', dpi=400, bbox_inches='tight')
# plt.grid(True)


# VẼ CẢ 2 ĐỒ THỊ HÌNH SIN VÀ COS

# x = np.arange(0, math.pi*2, 0.05)
# y = np.sin(x)
# z = np.cos(x)

# fig, axes = plt.subplots(2,2)

# axes[0,0].plot(x, y, color='b')
# axes[0,1].plot(x, z, color='r')



path_image = "VIETECH_DA_28.09.2023//Buoi16_DA.25.11.2023//chart_sin.png"

image = mpimg.imread(path_image)
x = np.arange(0, math.pi*3, 0.1)
y = np.sin(x)
fig, axes = plt.subplots(2,2, figsize = (5,5))
axes[0, 0].imshow(image)
axes[0, 1].plot(x, y, color='b')


plt.show()
